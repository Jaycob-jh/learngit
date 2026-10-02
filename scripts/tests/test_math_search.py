import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import math_search as search


class SearchTests(unittest.TestCase):
    def test_fences_preserve_source_lines_and_ignore_fake_headings(self):
        text = '~~~python\n# Fake title\n~~~\n# Actual title\n## Fourier\nText\n````text\n### Fake chapter\n```\n````\n## Bayes\nOther\n'
        title, sections = search.split_sections(text)
        self.assertEqual(title, 'Actual title')
        self.assertFalse(any('Fake' in s['heading'] for s in sections))
        for section in sections:
            self.assertEqual(section['text'], '\n'.join(text.splitlines()[section['line']-1:section['end']]))

    def test_same_fence_with_info_is_not_a_closing_fence(self):
        title, sections = search.split_sections('```python\n```text\n# Fake\n```\n# Real\nBody')
        self.assertEqual(title, 'Real')

    def test_links_labels_bare_urls_and_balanced_parentheses(self):
        refs = search.resource_links('[Course](https://example.org/course)\nhttps://example.org/book_(2020).\nhttps://example.org/course\n[bad](javascript:alert(1))')
        self.assertEqual(refs, [{'label':'Course','url':'https://example.org/course'}, {'label':'https://example.org/book_(2020)','url':'https://example.org/book_(2020)'}])

    def test_chinese_aliases_and_exact_option(self):
        self.assertIn('fourier', search.query_terms('傅里叶变换'))
        self.assertEqual(search.query_terms('傅里叶变换', False), ['傅里叶变换'])
        self.assertEqual(search.count_term('Bayesian Bayesianism Bayes', 'bayes'), 1)

    def test_category_filter_and_empty_query(self):
        docs = [{'path':'a','module':'数学主干','role':'数学专题','title':'Fourier','sections':[{'heading':'Definition','text':'Fourier','line':1,'end':1}],'url':'https://example.org/a'}, {'path':'b','module':'最优化课程','role':'课程与讲义','title':'Fourier','sections':[{'heading':'Definition','text':'Fourier','line':1,'end':1}],'url':'https://example.org/b'}]
        index = {'documents':docs}
        self.assertEqual([x['path'] for x in search.search(index, '傅里叶', '数学主干')], ['a'])
        self.assertEqual(search.search(index, ''), [])
        self.assertEqual(search.search(index, 'doesnotexist'), [])

    def test_script_termination_is_escaped(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template, output = root/'template.html', root/'page.html'
            template.write_text('<script>/*__KNOWLEDGE_INDEX__*/</script>', encoding='utf-8')
            search.write_page({'text':'</script><img src=x onerror=alert(1)>\u2028'}, template, output)
            page = output.read_text(encoding='utf-8')
            self.assertEqual(page.count('</script>'), 1)
            self.assertNotIn('<img', page)
            payload = page.split('const INDEX = ',1)[1].rsplit(';</script>',1)[0]
            self.assertIn('</script>', json.loads(payload)['text'])


if __name__ == '__main__':
    unittest.main()
