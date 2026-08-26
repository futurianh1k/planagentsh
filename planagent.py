from __future__ import annotations

import os
import sys
from pathlib import Path


DEFAULT_IDEA = "창업 도우미 AI 비서"


def build_prd(idea: str) -> str:
    market_context = (
        f"- PESTEL: {idea}는 개인정보 보호 규제와 AI 윤리 가이드라인의 영향을 받으므로 "
        "법적/사회적 요구사항을 초기 설계에 반영해야 한다.\n"
        "- Porter 5 Forces: 생성형 AI 도구 대체재가 많아 차별화된 실행 템플릿과 워크플로우 자동화가 중요하다.\n"
        "- SWOT: 강점은 빠른 기획 자동화, 약점은 도메인별 정확도 편차로 정리할 수 있다.\n"
        "- 정량 시장 규모/전환율 수치는 현재 출처 확인 전이므로 **검증 필요** 항목으로 유지한다."
    )

    strategy_context = (
        "- Lean Canvas: 문제(초기 기획 리소스 부족)와 고객군(초기 창업자/PM/PO)을 우선 정의한다.\n"
        "- 가치 제안: 아이디어 한 줄로 실행 가능한 기획 산출물까지 연결해 의사결정 시간을 단축한다.\n"
        "- 경쟁 우위: PESTEL에서 도출된 규제/신뢰 요건을 템플릿에 기본 반영해 실무 적합성을 높인다."
    )

    ux_context = (
        "- 페르소나: 리서치 경험이 제한적인 초기 창업자가 핵심 사용자다.\n"
        "- Customer Journey: 아이디어 입력 → 자동 분석 결과 확인 → 수정/보완 → 팀 공유.\n"
        "- 사용자 요구사항: 전략 단계의 가치 제안을 화면 플로우와 입력/출력 구조로 직접 연결한다.\n"
        "- 연결성 검증: 시장/전략에서 정의한 리스크와 차별화 포인트가 UX 요구사항에 반영되어야 한다."
    )

    product_context = (
        "- MVP: 서비스 아이디어 입력, 4개 에이전트 순차 분석, 컨텍스트 전달, 한글 PRD 생성/저장.\n"
        "- User Story: '초기 창업자로서, 아이디어를 입력하면 실행 가능한 PRD 초안을 빠르게 받고 싶다.'\n"
        "- Given-When-Then:\n"
        "  - Given 아이디어가 입력되면\n"
        "  - When 파이프라인이 순차 실행될 때\n"
        "  - Then `outputs/최종기획서.md`에 한국어 PRD가 저장된다.\n"
        "- PRD 품질 원칙: 확인되지 않은 수치는 사실로 단정하지 않고 **검증 필요**로 표시한다."
    )

    return f"""# PlanAgent Master PRD

## 서비스 아이디어

{idea}

## 목적

서비스 아이디어 한 줄을 바탕으로 시장 분석부터 개발용 PRD까지 연결된 초안을 자동 생성한다.

## 핵심 사용자

초기 스타트업 창업자, IT 서비스 PM/PO, 에이전시 기획자.

## Multi-Agent 파이프라인

1. Market Research Agent: PESTEL, Porter 5 Forces, SWOT
2. Strategy Agent: Lean Canvas, 가치 제안, 경쟁 우위
3. UX/Customer Agent: 페르소나, Customer Journey, 사용자 요구사항
4. Product Agent: MVP, User Story, Given-When-Then Acceptance Criteria, PRD

## Agent 1 결과 - Market Research

{market_context}

## Agent 2 결과 - Strategy

{strategy_context}

## Agent 3 결과 - UX/Customer

{ux_context}

## Agent 4 결과 - Product

{product_context}

## 검증 원칙

- 확인되지 않은 정량 데이터는 사실로 단정하지 않고 검증 필요 항목으로 표시한다.
- PESTEL과 전략 분석의 결과가 UX와 PRD에 연결되어야 한다.
- 실제 의사결정 전에는 생성 결과와 출처를 사람이 검토한다.

## 향후 확장

- 웹 검색 및 출처 추적
- Critic Agent 기반 논리 검증
- AI 활용 로그와 수정 이력
- PDF, DOCX, PPTX export
- RAG 및 기업용 온프레미스 모델 지원
"""


def write_prd(idea: str, base_dir: str | os.PathLike[str] = ".") -> Path:
    output_dir = Path(base_dir) / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "최종기획서.md"
    output_path.write_text(build_prd(idea), encoding="utf-8")
    return output_path


def main() -> int:
    idea = " ".join(sys.argv[1:]).strip() or DEFAULT_IDEA
    output_path = write_prd(idea)
    print(f"생성 완료: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
