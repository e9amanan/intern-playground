from todo.models import Task


def global_task_stats(request):
    """Injects pending task count into every template automatically."""
    # Assuming the user is logged in. Wrapped in a simple try/except for safety.
    try:
        if request.user.is_authenticated:
            pending_count = Task.objects.filter(
                assigned_user=request.user, status="PENDING"
            ).count()
        else:
            pending_count = 0
    except Exception:
        pending_count = 0  # Fallback

    return {"GLOBAL_PENDING_COUNT": pending_count}
