## Permissions and Groups Setup

This application uses Django custom permissions and groups to control access.

### Custom Permissions
Defined on the Book model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
-Admins: all permissions

### Enforcement
Permissions are enforced in views using the `@permission_required` decorator.

Example:
@permission_required("bookshelf.can_edit", raise_exception=True)

### Deployment documentation
HTTPS is enforced using an SSL/TLS certificate configured at the web server (Nginx) level.
All incoming HTTP traffic is redirected to HTTPS.
Django is configured to trust the reverse proxy via SECURE_PROXY_SSL_HEADER, enabling correct handling of secure cookies and redirects.
HSTS headers are enabled to instruct browsers to always use HTTPS for future requests.