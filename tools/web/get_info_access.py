from datetime import datetime
import pytz

def get_access_info(request):
    # Captura a data e hora atual com o fuso horário
    local_tz = pytz.timezone('America/Sao_Paulo')  # Ajuste o fuso horário conforme necessário
    now = datetime.now(local_tz)
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S %Z%z')

    user_info = {
        "ip_address": request.remote_addr,
        "user_agent": {
            "browser": request.user_agent.browser,
            "platform": request.user_agent.platform,
            "version": request.user_agent.version,
            "language": request.user_agent.language,
            "string": request.user_agent.string
        },
        "method": request.method,
        "url": request.url,
        "base_url": request.base_url,
        "path": request.path,
        "full_path": request.full_path,
        "script_root": request.script_root,
        "referrer": request.referrer,
        "headers": {key: value for key, value in request.headers.items()},
        "cookies": request.cookies,
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True),
        "data": request.data.decode('utf-8') if request.data else None,
        "files": {key: file.filename for key, file in request.files.items()},
        "content_type": request.content_type,
        "content_length": request.content_length,
        "mimetype": request.mimetype,
        "query_string": request.query_string.decode('utf-8'),
        "endpoint": request.endpoint,
        "blueprint": request.blueprint,
        "view_args": request.view_args,
        "timestamp":timestamp
    }
    return user_info
