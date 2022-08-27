# IoC Container

IoC Container pattern in implemented as follows.  
You may refer to [sequence diagram].  

## Implement Interactor classes

Implement the Interactor classes as the following rules apply.  

1. Define fields that injects as `pydantic.PrivateAttr` 
2. Specify Interface class that injects for type hint to the fields
3. Add `@inject` decorator to the `__init__()` method
4. Add `@singleton` decorator to the Interactor class

Exmaple: [todo.application.tasks.get_all.task_get_all_interactor.py]

## Implement Setting classes

Implement the Setting classes by inheriting `pydantic.BaseModel` to load settings from environment variables.  

Example: [todo.config.task_settings.py]

## Implement Module classes

Implement Module classes by inheriting `injector.Module`.  
At this time, bind Interface classes and concrete classes depending on field of Setting classes.  

Example: [todo.injector.task_module.py]

## Instantiate Injector class

Instantiate Injector class while specifying Module classes.  

Example: [todo.injector.injector.py]

## Implement InteractorBus class

Implement InteractorBus class for simplicity.  
Specifically, each constructor of the class using injector will no longer have to be changed.  

Example: [todo.injector.interactor_bus.py]

[sequence diagram]: ./sequence_diagrams.md#IoC-Container
[todo.application.tasks.get_all.task_get_all_interactor.py]: ../src/todo/application/tasks/get_all/task_get_all_interactor.py
[todo.config.task_settings.py]: ../src/todo/config/task_settings.py
[todo.injector.task_module.py]: ../src/todo/injector/task_module.py
[todo.injector.injector.py]: ../src/todo/injector/injector.py
[todo.injector.interactor_bus.py]: ../src/todo/injector/interactor_bus.py
