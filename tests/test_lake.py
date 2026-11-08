from app.build_lake import generate
def test_generated_prices_are_positive_and_labelled():
    df=generate(50); assert (df.price_kes>0).all(); assert df.is_synthetic.all()
def test_generator_reproducible():
    assert generate(20).equals(generate(20))
