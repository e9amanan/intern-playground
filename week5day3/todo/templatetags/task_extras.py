from django import template
from todo.models import Task

register = template.Library()


# Task 6: Custom Filter
@register.filter(name="status_badge")
def status_badge(status_code):
    """Converts a status code string into a CSS badge class name."""
    mapping = {
        "PENDING": "badge-warning",
        "IN_PROGRESS": "badge-info",
        "COMPLETED": "badge-success",
        "CANCELLED": "badge-danger",
    }
    return mapping.get(status_code, "badge-secondary")


# Task 6: Custom Simple Tag
@register.simple_tag
def get_recent_tasks(limit=5):
    """Fetches recent tasks directly within templates."""
    try:
        return Task.objects.order_by("-created_at")[:limit]
    except Exception:
        return []


# Problem 2: Custom Inclusion Tag
@register.inclusion_tag("partials/_priority_badge.html")
def render_priority_badge(priority_level):
    """Renders a partial template with contextual styling based on priority."""
    color_map = {"HIGH": "red", "MEDIUM": "orange", "LOW": "green"}
    return {
        "priority": priority_level,
        "color": color_map.get(str(priority_level).upper(), "gray"),
    }
