import pytest
import imaging.chroma_upsample_edge as mod

CASES = [
    ("bilinear_up", (1,)),
    ("border_extend", (1,)),
    ("block_align", (1,)),
    ("matrix_weights", (1,)),
    ("row_order", (1,)),
    ("edge_check", (1,)),
    ("determinism", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("convert", (1,)),
    ("metrics", (1,)),
    ("upsample", (1,)),
    ("plane_map", (1,)),
    ("output", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
