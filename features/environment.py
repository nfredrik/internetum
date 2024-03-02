from features.steps.assert_extensions import add_assert_extensions


def before_all(context):
    print('--before')

def before_feature(context, _):
    add_assert_extensions()