# 🤖 Discord Bot для кадрового управления ВС РФ
- **Группа `/moder`** - управление модераторами (ТОЛЬКО для администраторов):
  - `/moder add` - добавить модератора (роль или пользователя)
  - `/moder remove` - убрать модератора
  - `/moder list` - показать список модераторов
- **Группа `/admin`** - управление администраторами (ТОЛЬКО для администраторов):
  - `/admin add` - добавить администратора
  - `/admin remove` - убрать администратора
  - `/admin list` - показать список администраторов
- **Строгий контроль доступа** - команды настройки доступны ТОЛЬКО администраторам
- **Администраторы** - высший уровень доступа, имеют доступ ко всем командам и настройкам
- **Модераторы** - ограниченный уровень, могут только обрабатывать заявки через кнопки интерфейса
- **Иерархия модерации** - более высокие роли могут модерировать нижестоящих

## 🏗️ Структура проекта

```
├── app.py                  # Основной файл бота
├── requirements.txt        # Зависимости проекта
├── validate_bot.py         # Скрипт валидации системы
├── validate_config.py      # Проверка конфигурации
├── cogs/                   # Модули команд (расширения)
│   ├── __init__.py
│   └── channel_manager.py  # Управление каналами, модераторами, админами
├── utils/                  # Утилиты и вспомогательные функции
│   ├── __init__.py
│   ├── config_manager.py   # Работа с конфигурацией + новые функции
│   └── google_sheets.py    # Интеграция с Google Sheets
├── forms/                  # Формы и UI элементы
│   ├── __init__.py
│   ├── dismissal_form.py   # Форма увольнения + автоформатирование + защита от спама
│   ├── role_assignment_form.py # Формы заявок + автоформатирование + защита от спама
│   ├── medical_registration.py # Система записи к врачу с автозаполнением
│   └── settings/          # Модульная система настроек
│       ├── main.py        # Главное меню настроек
│       ├── channels.py    # Настройка каналов + пинг-роли чёрного списка
│       ├── role_config.py # Конфигурация ролей
│       ├── ping_settings.py # Настройка пингов для увольнений
│       └── excluded_roles.py # Роли-исключения
└── data/                   # Данные и конфигурация
    ├── config.json         # Основной файл конфигурации
    └── backups/           # Автоматические резервные копии
```

## 🚀 Основные функции

### 🛡️ Защита от спам-заявок (НОВОЕ!)
- **Антиспам для рапортов на увольнение** - пользователь не может подать новый рапорт, пока предыдущий не обработан
- **Антиспам для заявок на роли** - защита от множественных заявок на получение ролей
- **Интеллектуальная проверка** - система автоматически сканирует каналы на наличие необработанных заявок
- **Информативные сообщения** - пользователь получает понятное объяснение, почему заявка не принята

### ⚙️ Автоматическое форматирование статика
- **Универсальный ввод** - принимает форматы: `123456`, `123-456`, `123 456`, `12345`, `12-345`, `12 345`
- **Автоматическое форматирование** - все варианты преобразуются в стандартный формат `123-456` или `12-345`
- **Валидация** - отклонение некорректных статиков с подробным объяснением
- **Работает везде** - в формах увольнения и заявках на роли

### 👥 Иерархическая система прав доступа
- **Администраторы** - высший уровень доступа, могут модерировать всех (включая себя)
- **Модераторы** - средний уровень, могут модерировать обычных пользователей
- **Иерархия модерации** - более высокие роли могут модерировать нижестоящих
- **Защита от самомодерации** - модераторы не могут одобрить собственные рапорты (кроме админов)

### 🔧 Единая система команд
- **Группа `/moder`** - управление модераторами:
  - `/moder add` - добавить модератора (роль или пользователя)
  - `/moder remove` - убрать модератора
  - `/moder list` - показать список модераторов
- **Группа `/admin`** - управление администраторами:
  - `/admin add` - добавить администратора
  - `/admin remove` - убрать администратора
  - `/admin list` - показать список администраторов
- **Расширенный доступ к `/settings`** - теперь доступен пользовательским администраторам

### 📝 Система увольнений
- **Защита от спама** - невозможно подать повторный рапорт до обработки текущего
- **Автоформатирование статика** - поддержка различных форматов ввода
- **🚨 Автоматические увольнения** - автоматическое создание рапортов при выходе с сервера ✅
  - Причина "ПОТЕРЯ СПЕЦ. СВЯЗИ" для всех автоматических рапортов
  - Запрос статика у модератора при одобрении через модальное окно
  - **Система пингов по подразделениям** - уведомления командиров покинувшего ✅
  - Полная интеграция с существующей системой обработки
- Форма с полями: Имя, Статик (авто-формат), Причина
- **Умное управление ролями** - автоматическое снятие ролей при одобрении
- **Роли-исключения** - настройка ролей, которые не снимаются при увольнении
- **Система пингов** - автоматическое уведомление командиров по отделам
- **Иерархическая модерация** - права доступа на основе ролей и должностей
- Автоматическое изменение никнейма на "Уволен | Имя Фамилия"
- Интеграция с Google Sheets для ведения учёта
- Автоматическая отправка в чёрный список при увольнении менее чем через 5 дней
- Красивое оформление с embed и статусами обработки

### 🎖️ Система назначения ролей
- **Защита от спама** - одна заявка на пользователя до обработки текущей
- **Автоформатирование статика** - умная обработка различных форматов
- **Военные заявки** - форма с полями: Имя, Статик, Звание, Порядок набора
- **Гражданские заявки** - форма с полями: Имя, Статик, Фракция, Цель, Доказательства
- **Модерируемые заявки** - система одобрения/отклонения с указанием причин
- **Автоматическое изменение никнейма** - при одобрении военной заявки
- **Умная система исключений** - автоматическое снятие противоположных ролей

### 📦 Система склада
- **Защита от спама** - кулдаун 6 часов между запросами
- **Автоформатирование статика** - поддержка различных форматов ввода
- **Категорийная система** - оружие, бронежилеты, медикаменты, другое имущество
- **Гибкие лимиты** - настройка по должностям или званиям через `/settings`
- **Автоматическая валидация** - проверка лимитов с автокоррекцией количества
- **Умное автозаполнение** - данные из Google Sheets или ролей Discord
- **Пинги командиров** - уведомления по подразделениям через существующую систему
- **Модерация запросов** - кнопки "Выдать склад" / "Отклонить" для модераторов
- **Аудит выдач** - автоматическое логирование всех операций
- **Persistent кнопки** - система работает после перезапуска бота
- **Приказ № 256** - предустановленные лимиты согласно воинскому приказу

### 🏥 Система записи к врачу
- **Автозаполнение данных** - автоматическое заполнение ФИО и статика из Google Sheets
- **Раздельные типы записи** - отдельные роли доступа для ВВК и лекций
- **Прямая отправка заявок** - заявки отправляются напрямую в медицинский канал
- **Автоматическое сообщение с кнопками** - появляется при запуске бота и закрепляется
- **Настройка через /settings** - полная интеграция в систему настроек
- **Интеграция с Google Sheets** - использует данные из листа "Личный Состав"
- **Контроль доступа** - настраиваемые роли для разных типов медицинских услуг
- **Уведомления пользователей** - DM сообщения о статусе заявки
- **Интеграция с Google Sheets** - автоматическая запись при одобрении заявок
- **Автоматическая обработка рядовых** - полная автоматизация для звания "Рядовой"
- **Ручная обработка офицеров** - уведомления инструктора для высших званий

### 📊 Кадровый аудит
- Автоматическая система ведения учёта персонала
- Интеграция с Google Sheets для централизованного хранения
- Уведомления в канал аудита с полной информацией
- Отслеживание всех кадровых изменений

### 🚫 Чёрный список
- **Настройка пинг-ролей** - гибкая система уведомлений
- Автоматическое добавление при раннем увольнении (менее 5 дней службы)
- Форма с полями: Имя, Статик, Причина, Доказательства
- Строгий контроль и валидация данных

## 🔧 Команды бота

> **Права модераторов:**
> - ✅ Обрабатывать заявки на увольнение (кнопки ✅ Одобрить / ❌ Отказать)
> - ✅ Обрабатывать заявки на получение ролей (кнопки ✅ Одобрить / ❌ Отказать)
> - ✅ Модерировать пользователей согласно иерархии (не могут модерировать администраторов или себя)

### 🏠 Главная команда настройки (для администраторов)
- **`/settings`** - универсальная команда настройки с интерактивным интерфейсом
  - **Доступ ограничен** - только для администраторов Discord или пользовательских администраторов
  - Полный иерархический интерфейс для всех настроек

#### 📂 Настройка каналов
- **Канал увольнений** - настройка канала + системы пингов по отделам
- **Канал аудита** - настройка канала кадрового аудита  
- **Канал чёрного списка** - настройка канала + **НОВЫЕ пинг-роли для уведомлений**
- **Канал получения ролей** - полная настройка системы заявок
- **Канал медицинской регистрации** - настройка канала записи к врачу и ролей доступа

#### 🛡️ Роли-исключения
- Управление ролями, которые не снимаются при увольнении
- Добавление, удаление, очистка списка

#### 📦 Настройки склада
- **Каналы склада** - настройка каналов запросов и аудита
- **Режим лимитов** - переключение между лимитами по должностям/званиям
- **Управление лимитами** - добавление/изменение лимитов для должностей и званий
- **Кулдаун запросов** - настройка времени между запросами (по умолчанию 6 часов)

#### ⚙️ Просмотр настроек
- Полный обзор всех настроенных каналов, ролей и правил

### 👮 Управление модераторами (ТОЛЬКО ДЛЯ АДМИНИСТРАТОРОВ!)

**Группа команд `/moder`** - управление модераторами (требуют права администратора):
- **`/moder add`** `@роль_или_пользователь` - добавить модератора
- **`/moder remove`** `@роль_или_пользователь` - убрать модератора  
- **`/moder list`** - показать список всех модераторов

### 🔑 Управление администраторами (ТОЛЬКО ДЛЯ АДМИНИСТРАТОРОВ!)

**Группа команд `/admin`** - управление пользовательскими администраторами (требуют права администратора):
- **`/admin add`** `@роль_или_пользователь` - добавить администратора
- **`/admin remove`** `@роль_или_пользователь` - убрать администратора
- **`/admin list`** - показать список всех администраторов

### 🔐 Система прав доступа

**Иерархия прав:**
```
🔴 Администраторы Discord (Высшие права)
├── Полный доступ ко всем командам (/settings, /moder, /admin)
├── Могут модерировать всех, включая себя
└── Автоматически считаются администраторами бота

🟠 Пользовательские администраторы (Высокие права)  
├── Доступ к /settings (только через Discord админов)
├── Доступ к /admin командам (только через Discord админов)
├── Могут модерировать всех, включая себя
└── Управляются через /admin команды

🟡 Модераторы (Ограниченные права)
├── Обработка заявок на увольнение (кнопки одобрения/отклонения)
├── Обработка заявок на роли (кнопки одобрения/отклонения)
├── НЕ могут модерировать администраторов или себя
└── НЕ имеют доступа к командам настройки

🟢 Пользователи (Базовые права)
└── Отправка форм и заявок
```

## Настройка

### Требования
- Python 3.8 или выше
- Discord.py 2.0 или выше

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Настройка токена бота

Для работы бота необходимо создать в Discord Developer Portal приложение и бота, а затем указать токен одним из следующих способов:

1. Через переменную окружения:
```powershell
$env:DISCORD_TOKEN = "ваш_токен_бота"
```

2. Через файл `.env` в корне проекта:
```
DISCORD_TOKEN=ваш_токен_бота
```

3. Через файл `token.txt` в корне проекта (просто текстовый файл с токеном)

### Включение привилегированных интентов

⚠️ **ВАЖНО**: Для работы бота необходимо включить привилегированные интенты в Discord Developer Portal:

1. Перейдите на https://discord.com/developers/applications/
2. Выберите вашего бота
3. Перейдите во вкладку 'Bot'
4. Включите опции в секции 'Privileged Gateway Intents':
   - ✅ PRESENCE INTENT
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT
5. Сохраните изменения

## Запуск бота

```powershell
python app.py
```

## ✨ Особенности системы

### 📊 Валидация данных
- **Многоформатный статик** - автоматическая обработка различных вариантов ввода
- **Ограничения длины** - защита от чрезмерно длинных сообщений
- **Проверка корректности** - валидация всех полей перед отправкой
- **Понятные ошибки** - детальные объяснения проблем с вводом

### 🔄 Persistent Views
- **Устойчивость к перезапускам** - кнопки работают даже после перезапуска бота
- **Автоматическое восстановление** - умное восстановление интерфейса при старте
- **Защита от потери данных** - проверка существования сообщений с кнопками
- **Интеллектуальная синхронизация** - обновление только необходимых элементов

### 📢 Система пингов
#### Для увольнений:
- **Автоматическое определение отдела** - по ролям подающего рапорт
- **Гибкие настройки** - любое количество связок "отдел → командиры"
- **Множественные роли** - несколько ролей для уведомления на один отдел
- **Умная приоритизация** - выбор наивысшей роли в иерархии

#### Для чёрного списка:
- **Настройка через интерфейс** - кнопки добавления/удаления пинг-ролей  
- **Автоматические уведомления** - пинг назначенных ролей при отправке в чёрный список
- **Гибкое управление** - любое количество ролей для уведомлений
- **Интеграция с настройками** - полная интеграция в систему `/settings`

### 🎖️ Система назначения ролей
- **Модерируемые заявки** - все заявки проходят через модерацию
- **Автоматическое управление ролями** - умное снятие противоположных ролей
- **Интеграция с Google Sheets** - автоматическая запись одобренных заявок
- **Специальная обработка званий** - разная логика для рядовых и офицеров
- **Уведомления пользователей** - DM сообщения о статусе заявки

### 🔒 Безопасность
- **Контроль доступа** - строгая проверка прав на каждом уровне
- **Защита от самомодерации** - модераторы не могут одобрить собственные заявки
- **Иерархическая защита** - нижестоящие не могут модерировать вышестоящих
- **Эфемерные ответы** - настройки видны только администратору
- **Валидация входных данных** - защита от некорректных данных
- **Защита от спама** - предотвращение множественных заявок

### 🏗️ Архитектура
- **Модульная система** - легко расширяемые Cogs
- **Продвинутый конфиг-менеджер** - с резервным копированием и восстановлением
- **Отдельные модули форм** - изолированная логика для каждого типа формы
- **Настройки через интерфейс** - модульная система настроек с иерархическим меню

## Ключевые особенности

### ⚡ Persistent кнопки
- **Кнопки работают даже после перезапуска бота**
- Автоматическое восстановление интерфейса
- Надёжная работа без потери функциональности

### 🔧 Автоматическая настройка
- Проверка наличия кнопок в каналах при запуске
- Восстановление пропущенных сообщений
- Умная синхронизация команд

### 🔄 Интеллектуальное восстановление после перезапуска
- **Умное восстановление заявок** - только ожидающие модерации заявки получают кнопки управления
- **Пропуск обработанных заявок** - уже одобренные/отклоненные заявки не обновляются
- **Полное восстановление данных** - все поля заявки (звание, порядок набора, статик) восстанавливаются из embed'а
- **Работоспособность Google Sheets** - интеграция с таблицами работает даже после перезапуска бота
- **Безопасность данных** - предотвращение дублирования записей и ошибок восстановления

## 📁 Хранение данных

Бот использует файл `data/config.json` для хранения настроек с автоматическим резервным копированием в `data/backups/`. Конфигурация теперь включает новые поля для расширенной функциональности.

### Структура конфигурации:
```json
{
    "dismissal_channel": 123456789012345678,
    "audit_channel": 123456789012345679,
    "blacklist_channel": 123456789012345680,
    "role_assignment_channel": 123456789012345681,
    "medical_registration_channel": 123456789012345695,
    "military_roles": [123456789012345682],
    "civilian_roles": [123456789012345683],
    "excluded_roles": [123456789012345684, 123456789012345685],
    "ping_settings": {
        "123456789012345686": [123456789012345687, 123456789012345688]
    },
    "blacklist_role_mentions": [123456789012345689, 123456789012345690],
    "moderators": {
        "users": [123456789012345691],
        "roles": [123456789012345692]
    },
    "administrators": {
        "users": [123456789012345693],
        "roles": [123456789012345694]
    },
    "military_role_assignment_ping_roles": [123456789012345695],
    "civilian_role_assignment_ping_roles": [123456789012345696],
    "medical_role_id": 123456789012345697,
    "medical_vvk_allowed_roles": [123456789012345698, 123456789012345699],
    "medical_lecture_allowed_roles": [123456789012345700, 123456789012345701],    "warehouse_request_channel": 123456789012345702,
    "warehouse_audit_channel": 123456789012345703,
    "warehouse_submission_channel": 123456789012345704,
    "warehouse_cooldown_hours": 6,
    "warehouse_limits_mode": {
        "positions_enabled": true,
        "ranks_enabled": false
    },
    "warehouse_limits_positions": {
        "Оперативник ССО": {
            "оружие": 3,
            "бронежилеты": 10,
            "аптечки": 20,
            "обезболивающее": 8,
            "дефибрилляторы": 4,
            "weapon_restrictions": []
        }
    },
    "warehouse_limits_ranks": {
        "Рядовой": {
            "оружие": 2,
            "бронежилеты": 5,
            "аптечки": 10,
            "обезболивающее": 4,
            "дефибрилляторы": 0,
            "weapon_restrictions": ["Кольт М16", "АК-74М"]
        }
    }
}
```

### 🆕 Новые поля:
- **`administrators`** - пользовательские администраторы (отдельно от Discord админов)
  - `users` - ID пользователей-администраторов
  - `roles` - ID ролей-администраторов
- **`blacklist_role_mentions`** - роли для пинга при отправке в чёрный список
- **`military_roles`/`civilian_roles`** - массивы ролей (вместо одиночных полей)
- **`military_role_assignment_ping_roles`** - роли для пинга при военных заявках
- **`civilian_role_assignment_ping_roles`** - роли для пинга при гражданских заявках
- **`medical_registration_channel`** - канал для системы записи к врачу
- **`medical_role_id`** - роль медицинского персонала для получения заявок
- **`warehouse_request_channel`** - канал для запросов складского имущества (UI формы)
- **`warehouse_audit_channel`** - канал для аудита выдач со склада
- **`warehouse_submission_channel`** - канал для отправки готовых заявок модераторам
- **`warehouse_cooldown_hours`** - кулдаун между запросами в часах
- **`warehouse_limits_mode`** - режим работы лимитов (должности/звания)
- **`warehouse_limits_positions`** - лимиты по должностям с ограничениями оружия
- **`warehouse_limits_ranks`** - лимиты по званиям с ограничениями оружия
- **`medical_vvk_allowed_roles`** - роли с доступом к записи на ВВК
- **`medical_lecture_allowed_roles`** - роли с доступом к записи на лекции

### 🔄 Автоматическая миграция:
Бот автоматически обновляет старые конфигурации до нового формата при первом запуске.

## 🛡️ Система защиты конфигурации

### Автоматическая защита от потери настроек
Бот теперь оснащён **продвинутой системой резервного копирования**, которая защищает ваши настройки от потери:

- ✅ **Автоматические резервные копии** при каждом изменении настроек
- ✅ **Резервная копия при запуске** бота
- ✅ **Атомарная запись** предотвращает повреждение при сбоях
- ✅ **Автоматическое восстановление** из бэкапов при повреждении config.json
- ✅ **Умная очистка** старых копий (хранится 10 последних)

### Команды управления резервными копиями
- `/config-backup` - управление резервными копиями (создать, список, восстановить, статус)
- `/config-export` - экспорт конфигурации для переноса на другой сервер

### Типы резервных копий
- `startup` - при запуске бота
- `manual` - созданные вручную
- `before_save` - перед каждым сохранением
- `before_restore` - перед восстановлением

## 🚨 Устранение неполадок

### ✅ Потеря конфигурации (РЕШЕНО!)
**Эта проблема больше не актуальна** благодаря новой системе защиты:
- ✅ Автоматическое резервное копирование при каждом изменении
- ✅ Восстановление из резервных копий при повреждении
- ✅ Атомарная запись предотвращает повреждение файлов
- ✅ Умная очистка старых копий (хранится 10 последних)

### 🛡️ Проблемы с защитой от спама
**Если пользователь не может подать заявку:**
- Проверьте, нет ли у него необработанных заявок в соответствующем канале
- Убедитесь, что каналы настроены правильно в `/settings`
- Проверьте права бота на чтение истории сообщений

### ⚙️ Проблемы с автоформатированием
**Если статик не принимается:**
- Убедитесь, что статик содержит ровно 5 или 6 цифр
- Проверьте правильность формата: `123456`, `123-456`, `123 456`
- Удалите лишние символы и буквы

### 👮 Проблемы с правами доступа
**Если команды модерации недоступны:**
- Проверьте, добавлен ли пользователь через `/moder add` или `/admin add`
- Убедитесь, что пользователь имеет необходимые роли
- Discord админы автоматически имеют все права

### 📢 Проблемы с пинг-ролями
**Если уведомления не приходят:**
- Проверьте настройки пинг-ролей через `/settings`
- Убедитесь, что роли существуют и доступны боту
- Для чёрного списка: настройте роли через "Канал чёрного списка"

### 🔧 Общие проблемы

#### Ошибка при запуске
- Убедитесь, что установлены все зависимости: `pip install -r requirements.txt`
- Проверьте правильность токена бота
- Убедитесь, что включены привилегированные интенты

#### Команды не работают
- Проверьте права администратора у пользователя
- Убедитесь, что бот имеет права на отправку сообщений
- Проверьте синхронизацию команд (выполняется автоматически при старте)

#### Проблемы после перезапуска бота
- ✅ **Заявки обрабатываются заново**: Исправлено! Уже обработанные заявки пропускаются
- ✅ **Google Sheets не работает**: Исправлено! Все данные восстанавливаются полностью
- ✅ **Дублирование записей**: Защита от повторной обработки одобренных заявок
- ✅ **Потеря данных**: Система извлекает все поля из embed'ов сообщений

#### Кнопки не отвечают
- Система автоматически восстанавливает кнопки при старте
- Проверьте права бота в каналах
- Убедитесь, что каналы настроены через `/settings`

### 🔍 Диагностика системы
Для проверки состояния системы используйте:
- **`python validate_bot.py`** - полная проверка всех компонентов
- **`python validate_config.py`** - проверка конфигурации и резервных копий
- **`/settings`** - проверка текущих настроек через интерфейс

### 📞 Получение помощи
При возникновении проблем:
1. Запустите скрипт валидации: `python validate_bot.py`
2. Проверьте логи бота в консоли
3. Убедитесь, что все настройки корректны через `/settings`
4. Проверьте права бота на сервере
5. При необходимости восстановите конфигурацию из резервной копии

---

## 📚 Дополнительная документация

- **`validate_bot.py`** - Скрипт для проверки целостности системы
- **`validate_config.py`** - Утилита проверки конфигурации

---

**🎉 Система готова к полноценному использованию!**

Все функции протестированы и оптимизированы для стабильной работы в продакшн-среде. Бот обеспечивает надёжное управление кадровыми процессами с современными средствами защиты и удобным интерфейсом.

### 🔐 Система авторизации модераторов
**Правильная последовательность действий:**

1. ✅ **Назначение модератора** - администратор назначает пользователя модератором через `/moder add`
2. ✅ **Первое использование** - при первом одобрении/отклонении заявки система проверяет регистрацию в Google Sheets
3. ✅ **Автоматическая регистрация** - если модератор не найден в таблице, показывается форма регистрации
4. ✅ **Мгновенный доступ** - после регистрации модератор сразу может работать с системой

**Технические возможности:**
- **Умное извлечение данных** - автоматическое определение имени и статика из никнейма Discord
- **Множественные форматы никнеймов** - поддержка различных форматов: `ВА | Имя Фамилия`, `[Должность] Имя Фамилия`, `!![Звание] Имя Фамилия`
- **Валидация и форматирование** - автоматическое форматирование статика в модальном окне
- **Автоматический доступ к Google Sheets** - модераторы сразу получают права редактора
- **Защита от дублирования** - проверка существующих записей
- **Интеграция с Google Drive API** - автоматическое предоставление доступа к таблице
- **Надёжность** - система использует запасные варианты при ошибках

**Безопасность:**
- ❌ **Нельзя зарегистрироваться без роли модератора** - только назначенные модераторы могут регистрироваться в системе
- ✅ **Двойная проверка** - права проверяются и в config.json, и в Google Sheets
- ✅ **Аудит всех действий** - все записи в аудит используют корректные данные модератора