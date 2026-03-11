from backend.llm import query_hokkien_llm


def test_llm_response():
    user_input = "Li ho bo?"

    response = query_hokkien_llm(user_input)

    assert response is not None
    assert isinstance(response, str)
    assert "Hokkien:" in response or len(response) > 0


if __name__ == "__main__":
    print("Testing SEA-LION LLM...")
    result = query_hokkien_llm("Li ho bo?")
    print(result)