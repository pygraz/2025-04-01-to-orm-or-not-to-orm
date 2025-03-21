# Copyright (c) 2025 Python User Group Graz. Distributed under the MIT license.
from django.contrib import admin

from core.models import Issue, Label
from minitrack.settings import ADMIN_UI_KIND, AdminUiKind

if ADMIN_UI_KIND == AdminUiKind.BARE_BONES:
    # The bare-bones admin UI automatically generated from the model
    admin.site.register(Issue)
    admin.site.register(Label)

elif ADMIN_UI_KIND == AdminUiKind.ENHANCED:
    # An admin UI that already provides improved list display, search and sorting.

    @admin.register(Issue)
    class IssueAdmin(admin.ModelAdmin):
        list_display = ("title", "state", "assignee__username")
        list_filter = ("state", "assignee")
        ordering = ["title", "id"]
        search_fields = ("description", "title")

    @admin.register(Label)
    class LabelAdmin(admin.ModelAdmin):
        ordering = ["title"]

elif ADMIN_UI_KIND == AdminUiKind.FANCY:
    # An admin UI with some bells and whistles to show-case what's possible with extensions.
    pass  # TODO Dorian: Add fancy admin UI.
