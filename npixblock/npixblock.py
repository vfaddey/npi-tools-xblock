"""TO-DO: Write a description of what this XBlock is."""

from importlib.resources import files

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String


class NpiToolsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.

    link_url = String(
        default="https://example.com",
        scope=Scope.settings,
        help="URL, на который будет вести кнопка",
    )

    # Поле для хранения текста кнопки
    button_text = String(
        default="Перейти по ссылке",
        scope=Scope.settings,
        help="Текст, отображаемый на кнопке",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        return files(__package__).joinpath(path).read_text(encoding="utf-8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        Основное представление для студента.
        """
        print(context)
        html = self.render_template("static/html/npixblock.html", {
            "link_url": self.link_url,
            "button_text": self.button_text,
        })

        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/npixblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/npixblock.js"))
        frag.initialize_js('NpixBlock')
        return frag

    def studio_view(self, context=None):
        """
        Представление для редактирования в Studio.
        """
        html = self.render_template("static/html/npixblock.html", {
            "link_url": self.link_url,
            "button_text": self.button_text,
        })

        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/npixblock.css"))
        frag.add_javascript(self.resource_string("static/js/npixblock.js"))
        frag.initialize_js('NpixBlock', {
            "link_url": self.link_url,
            "button_text": self.button_text,
        })
        return frag
    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_settings(self, data, suffix=''):
        """
        Обработчик для сохранения настроек из Studio.
        """
        self.link_url = data.get('link_url', self.link_url)
        self.button_text = data.get('button_text', self.button_text)
        return {'result': 'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    def render_template(self, path, context):
        """Утилита для рендеринга HTML-шаблонов."""
        html = self.resource_string(path)
        return html.format(**context)

    @staticmethod
    def workbench_scenarios():
        """Сценарии для тестирования в Workbench."""
        return [
            ("NpixBlock",
             """<npixblock/>
             """),
        ]
