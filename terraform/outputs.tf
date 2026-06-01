output "service_url" {
  description = "URL publique du service déployé sur Render"
  value       = render_web_service.flask_app.urls
}

output "service_id" {
  description = "ID du service Render"
  value       = render_web_service.flask_app.id
}