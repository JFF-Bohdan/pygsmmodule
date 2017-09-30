from pygsmmodule.imei.imei import ImeiSupport


def test_can_check_valid_imeis():
    valid_imeis = [
        356938035643809,
        490154203237518,
        "356938035643809",
        358065019104265,
        "357805023984942",
        356938035643809
    ]

    for imei in valid_imeis:
        assert ImeiSupport.is_valid(imei)


def test_can_detect_invalid_imeis():
    invalid_imeis = [
        358065019104263,
        "357805023984941",
        356938035643801
    ]

    for imei in invalid_imeis:
        assert not ImeiSupport.is_valid(imei)


def test_generates_valid_imeis():
    imeis_to_test_count = 100

    for _ in range(imeis_to_test_count):
        value = ImeiSupport.generate_new()
        assert value is not None
        assert len(str(value)) == 16

        assert ImeiSupport.is_valid(value)


def test_generates_valid_sequental_imeis():
    current_imei = ImeiSupport.generate_new()
    assert ImeiSupport.is_valid(current_imei)

    imeis_to_test_count = 100
    for _ in range(imeis_to_test_count):
        current_imei = ImeiSupport.next(current_imei)
        assert ImeiSupport.is_valid(current_imei)


def test_generates_predicted_sequental_ids():
    expected_results = [
        (358065019104273, 358065019104281),
        (357805023984942, 357805023984959),
        (356938035643809, 356938035643817)
    ]

    for current_value, next_value in expected_results:
        generated_value = ImeiSupport.next(current_value)

        assert generated_value == next_value
