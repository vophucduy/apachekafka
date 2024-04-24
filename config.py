config = {
    "google_api_key": "<your google api>",
    # "youtube_playlist_id": "PL_Hyc1t0lCQEWN8pmeo3XuYfIeGhlsKQo",
    "youtube_playlist_id": "<your youtube playlist>",

    # "youtube_playlist_id": "PL2DsUt1fwwFlAjg6ePRBSwUhGvTecIYmv",

    "kafka": {
        "bootstrap.servers": "<your server>",
        "security.protocol": "sasl_ssl",
        "sasl.mechanism": "PLAIN",
        "sasl.username": "<your api>",
        "sasl.password": "<your api secret>",
    },
    "schema_registry": {
        "url": "<your endpoint>",
        "basic.auth.user.info": "<your credential api key>:<your credential api secret>",
    }
}
