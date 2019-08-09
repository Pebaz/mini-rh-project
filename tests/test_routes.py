import test_common
from flask import template_rendered
from contextlib import contextmanager
from rh.routes import *


@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_top10_genres():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/genres')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'top10.j2'
        assert context['category_name'] == 'genres'
        assert len(context['category']) == 10


def test_top10_actors():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/actors')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'top10.j2'
        assert context['category_name'] == 'actors'
        assert len(context['category']) == 10


def test_top10_directors():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/directors')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'top10.j2'
        assert context['category_name'] == 'directors'
        assert len(context['category']) == 10
