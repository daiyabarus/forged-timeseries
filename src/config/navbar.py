from streamlit_navigation_bar import st_navbar

# TAG: navbar is configuration for TOP the navigation bar


def navbar():
    pages = ["NR", "LTE", "GSM", "Upload", "Jarvis", "GitHub", "About"]
    urls = {"GitHub": "https://github.com/daiyabarus/forged-timeseries.git"}

    styles = {
        "nav": {
            "background-color": "royalblue",
            "justify-content": "center",
        },
        "img": {
            "padding-right": "14px",
        },
        "span": {
            "color": "white",
            "padding": "14px",
            "font-family": "Ericsson Hilda Light",
        },
        "active": {
            "background-color": "white",
            "color": "var(--text-color)",
            "font-weight": "normal",
            "padding": "14px",
        },
    }
    options = {
        "show_menu": True,
        "show_sidebar": True,
    }

    page = st_navbar(
        pages,
        urls=urls,
        styles=styles,
        options=options,
    )

    return page