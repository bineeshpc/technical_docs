import bruteforce


def test_bruteforce():
    p_s_r = [
        ('masala1', 'paneerbuttermasala', -1),
        ('masala', 'paneerbuttermasala', 12),
        ('bu', 'paneerbuttermasala', 6),
        ('pan', 'paneerbuttermasala', 0)
    ]

    for p, s, r in p_s_r:
        assert bruteforce.string_match(p, s) == r
