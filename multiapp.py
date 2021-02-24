import streamlit as st


class MultiApp:
    """Navigate across multiple Streamlit applications using the sidebar.

    Usage:
        import foo
        import bar

        app = MultiApp()

        app.add_app('Foo', foo.app)
        app.add_app('Bar', bar.app)

        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application to the list of apps to run.

        Parameters
        ----------
        func:
            Function to render the app.
        title:
            Title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            'title': title,
            'function': func
        })

    def run(self):
        app = st.sidebar.radio(
            'Choose a dashboard',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
