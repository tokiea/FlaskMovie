DEFAULT_BLUEPRINT = []


def init_view(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=blueprint.url_prefix)
