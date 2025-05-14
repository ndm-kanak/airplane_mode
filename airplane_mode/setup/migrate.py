from airplane_mode import utils


def after_migrate():
    utils.create_new_role(role="Airport Authority Personnel", enable_desk_access=True)
    utils.create_new_role(role="Fleet Manager", enable_desk_access=True)
    utils.create_new_role(role="Travel Agent", enable_desk_access=True)
    utils.create_new_role(role="Flight Crew Member", enable_desk_access=True)