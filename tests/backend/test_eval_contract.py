import pytest

from prozesspilot.eval.runner import evaluate_abstention, evaluate_source_ids


def test_acceptable_citation_passes():
    assert evaluate_source_ids(["src-a"], ["src-a"]) is True
    assert evaluate_source_ids(["src-a", "src-b"], ["src-b"]) is True


def test_unrelated_citation_fails():
    assert evaluate_source_ids(["src-a"], ["src-x"]) is False


def test_missing_citation_fails():
    assert evaluate_source_ids(["src-a"], []) is False


def test_deliberate_abstention_passes_when_expected():
    assert evaluate_abstention(True, False) is True


def test_unsupported_answering_fails_abstention_check():
    assert evaluate_abstention(True, True) is False


def test_malformed_labels_cannot_silently_pass():
    with pytest.raises(ValueError):
        evaluate_abstention(None, False)  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        evaluate_source_ids("not-a-list", ["src-a"])  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        evaluate_source_ids([123], ["src-a"])  # type: ignore[list-item]
    # empty acceptable set is "not applicable", never True
    assert evaluate_source_ids([], ["src-a"]) is None
