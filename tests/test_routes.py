"""
Test all routes for:

 * Correct template usage
 * Correct template parameter ingestion
 * HTTP status code
 * Failure
"""

import test_common
from flask import template_rendered
from contextlib import contextmanager
from rh.routes import *
from test_common import *


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


def test_root():
    with captured_templates(app) as templates:
        result = app.test_client().get('/')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'root.j2'
        

def test_not_found():
    with captured_templates(app) as templates:
        result = app.test_client().get('/foo')

        assert result.status_code == 404
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'not-found.j2'



def test_top10_genres():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/genres')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'top10.j2'
        assert context['category_name'] == 'genres'
        assert len(context['category']) == 10

        assert context['category'] == top_10_genres_by_profit


def test_top10_actors():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/actors')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'top10.j2'
        assert context['category_name'] == 'actors'
        assert len(context['category']) == 10

        assert context['category'] == top_10_actors_by_profit


def test_top10_directors():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/directors')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'top10.j2'
        assert context['category_name'] == 'directors'
        assert len(context['category']) == 10

        assert context['category'] == top_10_directors_by_profit


def test_top10_error():
    with captured_templates(app) as templates:
        result = app.test_client().get('/top10/foo')

        assert result.status_code == 404
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'not-found.j2'


def test_actor_info():
    with captured_templates(app) as templates:
        result = app.test_client().get(r'/actor/Harrison%20Ford')

        assert result.status_code == 200
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'actor.j2'
        assert context['actor_name'] == 'Harrison Ford'
        assert len(context['columns']) == 6
        assert len(context['column_names']) == 28


def test_actor_info_error():
    with captured_templates(app) as templates:
        result = app.test_client().get('/actor/foo')

        assert result.status_code == 404
        assert len(templates) == 1

        template, context = templates[0]

        assert template.name == 'not-found.j2'
