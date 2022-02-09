from flask import url_for
from flask_testing import TestCase
from app import app
from application import generate
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG=True)
        return app

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)

    def test_palette_post(self):
        response = self.client.post(url_for("get_palette"))
        self.assertEqual(response.status_code, 300)
    
    def test_palette_get(self):
        response = self.client.get(url_for("get_palette"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_about_get(self):
        response = self.client.get(url_for("about"))
        self.assertEqual(response.status_code, 200)

class TestHostname(TestBase):
    def test_hostname_set(self):
        with patch("application.routes.getenv") as get_hostname:
            get_hostname.return_value = "Test Host"
            response = self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Test Host", response.data)

def test_generate_palette():
    test_case = {
        "colour" : "(5, 5, 5)",
        "width" : 100
    }

    with patch("random.randint") as random_number:
        random_number.return_value = 5
        assert generate.palette()[0] == test_case

def test_generate_name():
    with patch("random.choice") as random_choice:
        with patch("random.randint") as random_number:
            random_choice.side_effect = ["testing,", "testing!", "123!"]
            random_number.return_value = 0
            assert generate.name() == "testing, testing! 123!"
