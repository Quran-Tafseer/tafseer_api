from prometheus_client import Counter


class MetricAPIGetMixin:
    metric_name = ""
    metric_desc = ""

    def get_metric_name(self):
        if self.metric_name == "":
            return self.get_view_name()
        return self.metric_name

    def get(self, request, *args, **kwargs):
        c = Counter(self.get_metric_name(), self.metric_desc)
        c.inc()
        return super(request, *args, **kwargs)