import tempfile
import unittest
from pathlib import Path

from planagent import build_prd, write_prd


class PlanAgentTest(unittest.TestCase):
    def test_build_prd_contains_required_sections(self):
        text = build_prd("창업 도우미 AI 비서")
        self.assertIn("## Multi-Agent 파이프라인", text)
        self.assertIn("Market Research Agent: PESTEL, Porter 5 Forces, SWOT", text)
        self.assertIn("Strategy Agent: Lean Canvas, 가치 제안, 경쟁 우위", text)
        self.assertIn("UX/Customer Agent: 페르소나, Customer Journey, 사용자 요구사항", text)
        self.assertIn("Product Agent: MVP, User Story, Given-When-Then Acceptance Criteria, PRD", text)
        self.assertIn("검증 필요", text)
        self.assertIn("PESTEL과 전략 분석의 결과가 UX와 PRD에 연결되어야 한다.", text)

    def test_write_prd_creates_expected_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = write_prd("테스트 아이디어", base_dir=tmpdir)
            self.assertEqual(output_path, Path(tmpdir) / "outputs" / "최종기획서.md")
            self.assertTrue(output_path.exists())
            content = output_path.read_text(encoding="utf-8")
            self.assertIn("테스트 아이디어", content)


if __name__ == "__main__":
    unittest.main()
