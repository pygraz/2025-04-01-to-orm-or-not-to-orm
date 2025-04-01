# Copyright (c) 2025 Python User Group Graz. Distributed under the MIT license.
from django.contrib import admin

from core.models import Issue, Label, Participant
from minitrack.settings import ADMIN_UI_KIND, AdminUiKind

if ADMIN_UI_KIND == AdminUiKind.BARE_BONES:
    # The bare-bones admin UI automatically generated from the model
    admin.site.register(Issue)
    admin.site.register(Label)
    admin.site.register(Paticipant)

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

    @admin.register(Participant)
    class ParticipantAdmin(admin.ModelAdmin):
        ordering = ["issue", "user", "role"]

elif ADMIN_UI_KIND == AdminUiKind.FANCY:
    # An admin UI with some bells and whistles to show-case what's possible with extensions.

    # Inlines ---------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#inlinemodeladmin-objects

    class ParticipantInlineAdmin(admin.StackedInline):
        model = Participant
        extra = 0
        classes = ["collapse"]
        readonly_fields = ["show"]  # method in class
        fields = ["user", "role", "show"]

    class IssueInlineAdmin(admin.TabularInline):
        model = Issue.labels.through
        extra = 0

    # Filter ----------------------------------------------------------------------------

    class IssueDemoFilter(admin.SimpleListFilter):
        title = "Active"
        parameter_name = "active"

        def lookups(self, request, model_admin):
            # usually : qs = model_admin.get_queryset(request)
            #           .. handle/filter/aggregate .. return [(attrib,text), ..]

            return [("yes", "Active"), ("no", "Inactive")]

        def queryset(self, request, queryset):
            if self.value() == "yes":
                return queryset.filter(state__in=["todo", "doing"])
            elif self.value() == "no":
                return queryset.filter(state="done")
            else:
                return queryset

    # Admin classes ---------------------------------------------------------------------

    @admin.register(Issue)
    class IssueAdmin(admin.ModelAdmin):
        list_display = ("title", "state", "assignee__username")
        list_filter = ("state", "assignee", IssueDemoFilter)
        ordering = ["title", "id"]
        search_fields = (
            "assignee__first_name",
            "assignee__username",
            "description",
            "title",
        )

        inlines = [
            ParticipantInlineAdmin,
        ]
        actions = ["demo_action_status_change"]

        @admin.action(description="change selected to 'done'")
        def demo_action_status_change(self, request, queryset):
            queryset.update(state="done")

    @admin.register(Label)
    class LabelAdmin(admin.ModelAdmin):
        ordering = ["title"]
        inlines = [
            IssueInlineAdmin,
        ]

    @admin.register(Participant)
    class ParticipantAdmin(admin.ModelAdmin):
        ordering = ["issue", "user", "role"]
