function NpixBlock(runtime, element, init_args) {
    var $element = $(element);
    var $studentView = $element.find('.npixblock-student-view');
    var $studioView = $element.find('.npixblock-studio-view');
    var $buttonTextInput = $element.find('.npixblock-button-text');
    var $linkUrlInput = $element.find('.npixblock-link-url');
    var $saveButton = $element.find('.npixblock-save-button');

    // Проверяем, находимся ли мы в Studio
    if (runtime.runtime_version && runtime.runtime_version() === 'studio') {
        $studentView.hide();
        $studioView.show();

        // Обработчик нажатия на кнопку "Сохранить"
        $saveButton.on('click', function() {
            var newButtonText = $buttonTextInput.val();
            var newLinkUrl = $linkUrlInput.val();

            // Отправляем данные на сервер через runtime.handlerUrl
            $.ajax({
                type: 'POST',
                url: runtime.handlerUrl(element, 'save_settings'),
                data: JSON.stringify({
                    button_text: newButtonText,
                    link_url: newLinkUrl
                }),
                contentType: 'application/json',
                success: function(response) {
                    if (response.result === 'success') {
                        alert('Настройки успешно сохранены!');
                        // Обновляем отображение кнопки в Studio
                        $element.find('.npixblock-button').text(newButtonText);
                        $element.find('a').attr('href', newLinkUrl);
                    } else {
                        alert('Ошибка при сохранении настроек.');
                    }
                },
                error: function() {
                    alert('Произошла ошибка при сохранении.');
                }
            });
        });
    } else {
        // Для студента показываем только кнопку
        $studentView.show();
        $studioView.hide();

        $element.find('.npixblock-button').on('click', function() {
            console.log("Кнопка нажата!");
        });
    }
}