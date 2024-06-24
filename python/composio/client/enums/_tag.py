"""
Tag enums.
"""

from composio.client.enums.base import TAGS_CACHE, TagData, _AnnotatedEnum, enum


@enum
class Tag(_AnnotatedEnum[TagData], path=TAGS_CACHE):
    """Tag object."""

    ASANA_ALLOCATIONS: "Tag"
    ASANA_ATTACHMENTS: "Tag"
    ASANA_AUDIT_LOG_API: "Tag"
    ASANA_BATCH_API: "Tag"
    ASANA_CUSTOM_FIELD_SETTINGS: "Tag"
    ASANA_CUSTOM_FIELDS: "Tag"
    ASANA_EVENTS: "Tag"
    ASANA_GOAL_RELATIONSHIPS: "Tag"
    ASANA_GOALS: "Tag"
    ASANA_JOBS: "Tag"
    ASANA_MEMBERSHIPS: "Tag"
    ASANA_ORGANIZATION_EXPORTS: "Tag"
    ASANA_PORTFOLIO_MEMBERSHIPS: "Tag"
    ASANA_PORTFOLIOS: "Tag"
    ASANA_PROJECT_BRIEFS: "Tag"
    ASANA_PROJECT_MEMBERSHIPS: "Tag"
    ASANA_PROJECT_STATUSES: "Tag"
    ASANA_PROJECT_TEMPLATES: "Tag"
    ASANA_PROJECTS: "Tag"
    ASANA_RULES: "Tag"
    ASANA_SECTIONS: "Tag"
    ASANA_STATUS_UPDATES: "Tag"
    ASANA_STORIES: "Tag"
    ASANA_TAGS: "Tag"
    ASANA_TASK_TEMPLATES: "Tag"
    ASANA_TASKS: "Tag"
    ASANA_TEAM_MEMBERSHIPS: "Tag"
    ASANA_TEAMS: "Tag"
    ASANA_TIME_PERIODS: "Tag"
    ASANA_TIME_TRACKING_ENTRIES: "Tag"
    ASANA_TYPEAHEAD: "Tag"
    ASANA_USER_TASK_LISTS: "Tag"
    ASANA_USERS: "Tag"
    ASANA_WEBHOOKS: "Tag"
    ASANA_WORKSPACE_MEMBERSHIPS: "Tag"
    ASANA_WORKSPACES: "Tag"
    ATTIO_ATTRIBUTES: "Tag"
    ATTIO_COMMENTS: "Tag"
    ATTIO_ENTRIES: "Tag"
    ATTIO_LISTS: "Tag"
    ATTIO_META: "Tag"
    ATTIO_NOTES: "Tag"
    ATTIO_OBJECTS: "Tag"
    ATTIO_RECORDS: "Tag"
    ATTIO_TASKS: "Tag"
    ATTIO_THREADS: "Tag"
    ATTIO_WEBHOOKS: "Tag"
    ATTIO_WORKSPACE_MEMBERS: "Tag"
    BREVO_ACCOUNT: "Tag"
    BREVO_COMPANIES: "Tag"
    BREVO_CONTACTS: "Tag"
    BREVO_CONVERSATIONS: "Tag"
    BREVO_COUPONS: "Tag"
    BREVO_DEALS: "Tag"
    BREVO_DOMAINS: "Tag"
    BREVO_ECOMMERCE: "Tag"
    BREVO_EMAIL_CAMPAIGNS: "Tag"
    BREVO_EVENT: "Tag"
    BREVO_EXTERNAL_FEEDS: "Tag"
    BREVO_FILES: "Tag"
    BREVO_INBOUND_PARSING: "Tag"
    BREVO_MASTER_ACCOUNT: "Tag"
    BREVO_NOTES: "Tag"
    BREVO_PROCESS: "Tag"
    BREVO_RESELLER: "Tag"
    BREVO_SMS_CAMPAIGNS: "Tag"
    BREVO_SENDERS: "Tag"
    BREVO_TASKS: "Tag"
    BREVO_TRANSACTIONAL_SMS: "Tag"
    BREVO_TRANSACTIONAL_WHATSAPP: "Tag"
    BREVO_TRANSACTIONAL_EMAILS: "Tag"
    BREVO_USER: "Tag"
    BREVO_WEBHOOKS: "Tag"
    BREVO_WHATSAPP_CAMPAIGNS: "Tag"
    CLICKUP_ATTACHMENTS: "Tag"
    CLICKUP_AUTHORIZATION: "Tag"
    CLICKUP_COMMENTS: "Tag"
    CLICKUP_CUSTOM_FIELDS: "Tag"
    CLICKUP_CUSTOM_TASK_TYPES: "Tag"
    CLICKUP_FOLDERS: "Tag"
    CLICKUP_GOALS: "Tag"
    CLICKUP_GUESTS: "Tag"
    CLICKUP_LISTS: "Tag"
    CLICKUP_MEMBERS: "Tag"
    CLICKUP_ROLES: "Tag"
    CLICKUP_SHARED_HIERARCHY: "Tag"
    CLICKUP_SPACES: "Tag"
    CLICKUP_TAGS: "Tag"
    CLICKUP_TASK_CHECKLISTS: "Tag"
    CLICKUP_TASK_RELATIONSHIPS: "Tag"
    CLICKUP_TASK_TEMPLATES: "Tag"
    CLICKUP_TASKS: "Tag"
    CLICKUP_TEAMS___USER_GROUPS: "Tag"
    CLICKUP_TEAMS___WORKSPACES: "Tag"
    CLICKUP_TIME_TRACKING: "Tag"
    CLICKUP_TIME_TRACKING__LEGACY_: "Tag"
    CLICKUP_USERS: "Tag"
    CLICKUP_VIEWS: "Tag"
    CLICKUP_WEBHOOKS: "Tag"
    ELEVENLABS_PRONUNCIATION_DICTIONARY: "Tag"
    ELEVENLABS_AUDIO_NATIVE: "Tag"
    ELEVENLABS_DUBBING: "Tag"
    ELEVENLABS_MODELS: "Tag"
    ELEVENLABS_PROJECTS: "Tag"
    ELEVENLABS_SAMPLES: "Tag"
    ELEVENLABS_SPEECH_HISTORY: "Tag"
    ELEVENLABS_SPEECH_TO_SPEECH: "Tag"
    ELEVENLABS_TEXT_TO_SPEECH: "Tag"
    ELEVENLABS_USER: "Tag"
    ELEVENLABS_VOICE_GENERATION: "Tag"
    ELEVENLABS_VOICES: "Tag"
    ELEVENLABS_WORKSPACE: "Tag"
    FIGMA_ACTIVITY_LOGS: "Tag"
    FIGMA_COMMENT_REACTIONS: "Tag"
    FIGMA_COMMENTS: "Tag"
    FIGMA_COMPONENT_SETS: "Tag"
    FIGMA_COMPONENTS: "Tag"
    FIGMA_DEV_RESOURCES: "Tag"
    FIGMA_FILES: "Tag"
    FIGMA_PAYMENTS: "Tag"
    FIGMA_PROJECTS: "Tag"
    FIGMA_STYLES: "Tag"
    FIGMA_USERS: "Tag"
    FIGMA_VARIABLES: "Tag"
    FIGMA_WEBHOOKS: "Tag"
    GITHUB_ACTIONS: "Tag"
    GITHUB_ACTIVITY: "Tag"
    GITHUB_APPS: "Tag"
    GITHUB_BILLING: "Tag"
    GITHUB_CHECKS: "Tag"
    GITHUB_CLASSROOM: "Tag"
    GITHUB_CODE: "Tag"
    GITHUB_CODE_SCANNING: "Tag"
    GITHUB_CODES_OF_CONDUCT: "Tag"
    GITHUB_CODESPACES: "Tag"
    GITHUB_COPILOT: "Tag"
    GITHUB_DEPENDABOT: "Tag"
    GITHUB_DEPENDENCY_GRAPH: "Tag"
    GITHUB_EMOJIS: "Tag"
    GITHUB_GISTS: "Tag"
    GITHUB_GIT: "Tag"
    GITHUB_GITIGNORE: "Tag"
    GITHUB_IMPORTANT: "Tag"
    GITHUB_INTERACTIONS: "Tag"
    GITHUB_ISSUES: "Tag"
    GITHUB_LICENSES: "Tag"
    GITHUB_MARKDOWN: "Tag"
    GITHUB_META: "Tag"
    GITHUB_MIGRATIONS: "Tag"
    GITHUB_OIDC: "Tag"
    GITHUB_ORGS: "Tag"
    GITHUB_PACKAGES: "Tag"
    GITHUB_PROJECTS: "Tag"
    GITHUB_PULLS: "Tag"
    GITHUB_RATE_LIMIT: "Tag"
    GITHUB_REACTIONS: "Tag"
    GITHUB_REPOS: "Tag"
    GITHUB_SEARCH: "Tag"
    GITHUB_SECRET_SCANNING: "Tag"
    GITHUB_SECURITY_ADVISORIES: "Tag"
    GITHUB_TEAMS: "Tag"
    GITHUB_USERS: "Tag"
    LISTENNOTES_DIRECTORY_API: "Tag"
    LISTENNOTES_INSIGHTS_API: "Tag"
    LISTENNOTES_PLAYLIST_API: "Tag"
    LISTENNOTES_PODCASTER_API: "Tag"
    LISTENNOTES_SEARCH_API: "Tag"
    NASA_ORGANIZATION: "Tag"
    NASA_PROJECT: "Tag"
    NASA_RESOURCE: "Tag"
    OKTA_APPLICATION: "Tag"
    OKTA_AUTHENTICATOR: "Tag"
    OKTA_AUTHORIZATIONSERVER: "Tag"
    OKTA_BRAND: "Tag"
    OKTA_DOMAIN: "Tag"
    OKTA_EVENTHOOK: "Tag"
    OKTA_FEATURE: "Tag"
    OKTA_GROUP: "Tag"
    OKTA_GROUPSCHEMA: "Tag"
    OKTA_IDENTITYPROVIDER: "Tag"
    OKTA_INLINEHOOK: "Tag"
    OKTA_LINKEDOBJECT: "Tag"
    OKTA_LOG: "Tag"
    OKTA_NETWORKZONE: "Tag"
    OKTA_ORG: "Tag"
    OKTA_POLICY: "Tag"
    OKTA_PROFILEMAPPING: "Tag"
    OKTA_SESSION: "Tag"
    OKTA_SUBSCRIPTION: "Tag"
    OKTA_TEMPLATE: "Tag"
    OKTA_THREATINSIGHT: "Tag"
    OKTA_TRUSTEDORIGIN: "Tag"
    OKTA_USER: "Tag"
    OKTA_USERFACTOR: "Tag"
    OKTA_USERSCHEMA: "Tag"
    OKTA_USERTYPE: "Tag"
    PAGERDUTY_ABILITIES: "Tag"
    PAGERDUTY_ADD_ONS: "Tag"
    PAGERDUTY_ALERT_GROUPING_SETTINGS: "Tag"
    PAGERDUTY_ANALYTICS: "Tag"
    PAGERDUTY_AUDIT: "Tag"
    PAGERDUTY_AUTOMATION_ACTIONS: "Tag"
    PAGERDUTY_BUSINESS_SERVICES: "Tag"
    PAGERDUTY_CHANGE_EVENTS: "Tag"
    PAGERDUTY_CUSTOM_FIELDS: "Tag"
    PAGERDUTY_ESCALATION_POLICIES: "Tag"
    PAGERDUTY_EVENT_ORCHESTRATIONS: "Tag"
    PAGERDUTY_EXTENSION_SCHEMAS: "Tag"
    PAGERDUTY_EXTENSIONS: "Tag"
    PAGERDUTY_INCIDENT_WORKFLOWS: "Tag"
    PAGERDUTY_INCIDENTS: "Tag"
    PAGERDUTY_LICENSES: "Tag"
    PAGERDUTY_LOG_ENTRIES: "Tag"
    PAGERDUTY_MAINTENANCE_WINDOWS: "Tag"
    PAGERDUTY_NOTIFICATIONS: "Tag"
    PAGERDUTY_ON_CALLS: "Tag"
    PAGERDUTY_PAUSED_INCIDENT_REPORTS: "Tag"
    PAGERDUTY_PRIORITIES: "Tag"
    PAGERDUTY_RESPONSE_PLAYS: "Tag"
    PAGERDUTY_RULESETS: "Tag"
    PAGERDUTY_SCHEDULES: "Tag"
    PAGERDUTY_SERVICE_DEPENDENCIES: "Tag"
    PAGERDUTY_SERVICES: "Tag"
    PAGERDUTY_STANDARDS: "Tag"
    PAGERDUTY_STATUS_DASHBOARDS: "Tag"
    PAGERDUTY_STATUS_PAGES: "Tag"
    PAGERDUTY_TAGS: "Tag"
    PAGERDUTY_TEAMS: "Tag"
    PAGERDUTY_TEMPLATES: "Tag"
    PAGERDUTY_USERS: "Tag"
    PAGERDUTY_VENDORS: "Tag"
    PAGERDUTY_WEBHOOKS: "Tag"
    SLACK_ADMIN: "Tag"
    SLACK_ADMIN_APPS: "Tag"
    SLACK_ADMIN_APPS_APPROVED: "Tag"
    SLACK_ADMIN_APPS_REQUESTS: "Tag"
    SLACK_ADMIN_APPS_RESTRICTED: "Tag"
    SLACK_ADMIN_CONVERSATIONS: "Tag"
    SLACK_ADMIN_CONVERSATIONS_EKM: "Tag"
    SLACK_ADMIN_CONVERSATIONS_RESTRICTACCESS: "Tag"
    SLACK_ADMIN_EMOJI: "Tag"
    SLACK_ADMIN_INVITEREQUESTS: "Tag"
    SLACK_ADMIN_INVITEREQUESTS_APPROVED: "Tag"
    SLACK_ADMIN_INVITEREQUESTS_DENIED: "Tag"
    SLACK_ADMIN_TEAMS: "Tag"
    SLACK_ADMIN_TEAMS_ADMINS: "Tag"
    SLACK_ADMIN_TEAMS_OWNERS: "Tag"
    SLACK_ADMIN_TEAMS_SETTINGS: "Tag"
    SLACK_ADMIN_USERGROUPS: "Tag"
    SLACK_ADMIN_USERS: "Tag"
    SLACK_ADMIN_USERS_SESSION: "Tag"
    SLACK_API: "Tag"
    SLACK_APPS: "Tag"
    SLACK_APPS_EVENT_AUTHORIZATIONS: "Tag"
    SLACK_APPS_PERMISSIONS: "Tag"
    SLACK_APPS_PERMISSIONS_RESOURCES: "Tag"
    SLACK_APPS_PERMISSIONS_SCOPES: "Tag"
    SLACK_APPS_PERMISSIONS_USERS: "Tag"
    SLACK_AUTH: "Tag"
    SLACK_BOTS: "Tag"
    SLACK_CALLS: "Tag"
    SLACK_CALLS_PARTICIPANTS: "Tag"
    SLACK_CHAT: "Tag"
    SLACK_CHAT_SCHEDULEDMESSAGES: "Tag"
    SLACK_CONVERSATIONS: "Tag"
    SLACK_DIALOG: "Tag"
    SLACK_DND: "Tag"
    SLACK_EMOJI: "Tag"
    SLACK_FILES: "Tag"
    SLACK_FILES_COMMENTS: "Tag"
    SLACK_FILES_REMOTE: "Tag"
    SLACK_IMPORTANT: "Tag"
    SLACK_MIGRATION: "Tag"
    SLACK_OAUTH: "Tag"
    SLACK_OAUTH_V2: "Tag"
    SLACK_PINS: "Tag"
    SLACK_REACTIONS: "Tag"
    SLACK_REMINDERS: "Tag"
    SLACK_RTM: "Tag"
    SLACK_SEARCH: "Tag"
    SLACK_STARS: "Tag"
    SLACK_TEAM: "Tag"
    SLACK_TEAM_PROFILE: "Tag"
    SLACK_USERGROUPS: "Tag"
    SLACK_USERGROUPS_USERS: "Tag"
    SLACK_USERS: "Tag"
    SLACK_USERS_PROFILE: "Tag"
    SLACK_VIEWS: "Tag"
    SLACK_WORKFLOWS: "Tag"
    SLACKBOT_API: "Tag"
    SLACKBOT_APPS: "Tag"
    SLACKBOT_APPS_EVENT_AUTHORIZATIONS: "Tag"
    SLACKBOT_APPS_PERMISSIONS: "Tag"
    SLACKBOT_APPS_PERMISSIONS_RESOURCES: "Tag"
    SLACKBOT_APPS_PERMISSIONS_SCOPES: "Tag"
    SLACKBOT_APPS_PERMISSIONS_USERS: "Tag"
    SLACKBOT_AUTH: "Tag"
    SLACKBOT_BOTS: "Tag"
    SLACKBOT_CALLS: "Tag"
    SLACKBOT_CALLS_PARTICIPANTS: "Tag"
    SLACKBOT_CHAT: "Tag"
    SLACKBOT_CHAT_SCHEDULEDMESSAGES: "Tag"
    SLACKBOT_CONVERSATIONS: "Tag"
    SLACKBOT_DIALOG: "Tag"
    SLACKBOT_DND: "Tag"
    SLACKBOT_EMOJI: "Tag"
    SLACKBOT_FILES: "Tag"
    SLACKBOT_FILES_COMMENTS: "Tag"
    SLACKBOT_FILES_REMOTE: "Tag"
    SLACKBOT_IMPORTANT: "Tag"
    SLACKBOT_MIGRATION: "Tag"
    SLACKBOT_OAUTH: "Tag"
    SLACKBOT_OAUTH_V2: "Tag"
    SLACKBOT_PINS: "Tag"
    SLACKBOT_REACTIONS: "Tag"
    SLACKBOT_REMINDERS: "Tag"
    SLACKBOT_RTM: "Tag"
    SLACKBOT_STARS: "Tag"
    SLACKBOT_TEAM: "Tag"
    SLACKBOT_TEAM_PROFILE: "Tag"
    SLACKBOT_USERGROUPS: "Tag"
    SLACKBOT_USERGROUPS_USERS: "Tag"
    SLACKBOT_USERS: "Tag"
    SLACKBOT_USERS_PROFILE: "Tag"
    SLACKBOT_VIEWS: "Tag"
    SLACKBOT_WORKFLOWS: "Tag"
    SPOTIFY_ALBUMS: "Tag"
    SPOTIFY_ARTISTS: "Tag"
    SPOTIFY_AUDIOBOOKS: "Tag"
    SPOTIFY_CATEGORIES: "Tag"
    SPOTIFY_CHAPTERS: "Tag"
    SPOTIFY_EPISODES: "Tag"
    SPOTIFY_GENRES: "Tag"
    SPOTIFY_LIBRARY: "Tag"
    SPOTIFY_MARKETS: "Tag"
    SPOTIFY_PLAYER: "Tag"
    SPOTIFY_PLAYLISTS: "Tag"
    SPOTIFY_SEARCH: "Tag"
    SPOTIFY_SHOWS: "Tag"
    SPOTIFY_TRACKS: "Tag"
    SPOTIFY_USERS: "Tag"
    STRAVA_ACTIVITIES: "Tag"
    STRAVA_ATHLETES: "Tag"
    STRAVA_CLUBS: "Tag"
    STRAVA_GEARS: "Tag"
    STRAVA_ROUTES: "Tag"
    STRAVA_SEGMENTEFFORTS: "Tag"
    STRAVA_SEGMENTS: "Tag"
    STRAVA_STREAMS: "Tag"
    STRAVA_UPLOADS: "Tag"
    TASKADE_AGENT: "Tag"
    TASKADE_FOLDER: "Tag"
    TASKADE_ME: "Tag"
    TASKADE_PROJECT: "Tag"
    TASKADE_TASK: "Tag"
    TASKADE_WORKSPACE: "Tag"
    TRELLO_ACTION: "Tag"
    TRELLO_BATCH: "Tag"
    TRELLO_BOARD: "Tag"
    TRELLO_CARD: "Tag"
    TRELLO_CHECKLIST: "Tag"
    TRELLO_LABEL: "Tag"
    TRELLO_LIST: "Tag"
    TRELLO_MEMBER: "Tag"
    TRELLO_NOTIFICATION: "Tag"
    TRELLO_ORGANIZATION: "Tag"
    TRELLO_SEARCH: "Tag"
    TRELLO_SESSION: "Tag"
    TRELLO_TOKEN: "Tag"
    TRELLO_TYPE: "Tag"
    TRELLO_WEBHOOK: "Tag"
    WHATSAPP_APPLICATION: "Tag"
    WHATSAPP_BACKUP_RESTORE: "Tag"
    WHATSAPP_BUSINESS_PROFILE: "Tag"
    WHATSAPP_CERTIFICATES: "Tag"
    WHATSAPP_CONTACTS: "Tag"
    WHATSAPP_GROUPS: "Tag"
    WHATSAPP_HEALTH: "Tag"
    WHATSAPP_MEDIA: "Tag"
    WHATSAPP_MESSAGES: "Tag"
    WHATSAPP_PROFILE: "Tag"
    WHATSAPP_REGISTRATION: "Tag"
    WHATSAPP_TWO_STEP_VERIFICATION: "Tag"
    WHATSAPP_USERS: "Tag"
    ZOOM_ARCHIVING: "Tag"
    ZOOM_CLOUD_RECORDING: "Tag"
    ZOOM_DEVICES: "Tag"
    ZOOM_H323_DEVICES: "Tag"
    ZOOM_MEETINGS: "Tag"
    ZOOM_PAC: "Tag"
    ZOOM_REPORTS: "Tag"
    ZOOM_SIP_PHONE: "Tag"
    ZOOM_TSP: "Tag"
    ZOOM_TRACKING_FIELD: "Tag"
    ZOOM_WEBINARS: "Tag"

    @property
    def app(self) -> str:
        """App name for this tag."""
        return self.load().app

    @property
    def value(self) -> str:
        """Tag string."""
        return self.load().value
