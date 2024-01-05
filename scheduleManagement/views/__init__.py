from .templates import HomeRequestHandler, UserRequestHandler  # noqa: F401

from .create import (
    UserCreateRequestHandler,  # noqa: F401
    CourseCreateRequestHandler,  # noqa: F401
    DisciplineCreateRequestHandler,  # noqa: F401
    ScheduleCreateRequestHandler,  # noqa: F401
)

from .list import (
    CourseListRequestHandler,  # noqa: F401
    DisciplineListRequestHandler,  # noqa: F401
    ScheduleListRequestHandler,  # noqa: F401
)

from .update import (
    UserUpdateRequestHandler,  # noqa: F401
    CourseUpdateRequestHandler,  # noqa: F401
    DisciplineUpdateRequestHandler,  # noqa: F401
    ScheduleUpdateRequestHandler,  # noqa: F401
)

from .details import (
    CourseDetailsRequestHandler,  # noqa: F401
    DisciplineDetailsRequestHandler,  # noqa: F401
    ScheduleDetailsRequestHandler,  # noqa: F401
)

from .delete import (
    CourseDeleteRequestHandler,  # noqa: F401
    DisciplineDeleteRequestHandler,  # noqa: F401
    ScheduleDeleteRequestHandler,  # noqa: F401
)
