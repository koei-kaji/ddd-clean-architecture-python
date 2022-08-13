# Directory Structure

These codes are based on Clean Architecture.  

## Core Module: `todo`

```txt
# tree -I __pycache__ -d ./src/todo/

./src/todo/
├── application             # Application Services
│   ├── abc
│   └── tasks
│       ├── commons
│       ├── delete
│       ├── get_all
│       ├── get_by_id
│       ├── register
│       └── update
├── config
├── domain
│   └── models              # Domain Models
│       └── tasks
├── infrastructure          # Concrete Factory, QueryService and Repository by infrastructure
│   └── in_memory
│       └── tasks
└── injector                # IoC Container
```

## External API Modules

### `rest_api`

```txt
# tree -I __pycache__ -d ./src/rest_api/

./src/rest_api/
├── main.py                 # Endpoints
└── models                  # View Models
    ├── healthz
    └── tasks
        ├── commons
        ├── delete
        ├── get
        ├── patch
        └── post
```

#### Reference: `gunicorn.conf.py`

```txt
./src/
└── gunicorn.conf.py
```

## Other Modules

### `custom_pydantic`

```txt
# tree -I __pycache__ ./src/custom_pydantic/

./src/custom_pydantic/      
├── config.py               # Custom config of pydantic.config.BaseConfig
└── __init__.py
```
