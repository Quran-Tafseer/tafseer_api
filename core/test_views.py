from unittest import TestCase

from rest_framework import generics
from .views import MetricAPIGetMixin


class TestView(generics.ListAPIView, MetricAPIGetMixin):
    pass


class TestMetricView(TestCase):
    def test_view_get_metric_name(self):
        test_view = TestView()
        test_view.metric_name = "test_metric"

        self.assertEqual("test_metric", test_view.get_metric_name())

    def test_view_get_metric_name_empty(self):
        test_view = TestView()

        self.assertEqual("Test", test_view.get_metric_name())
