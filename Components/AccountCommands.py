import Command


class CreateAccount(Command.Command):

    def __init__(self, environment):
        self.environment = environment
    """
        args is a list containing the following:
            ["create_account", username, password, role]
    """
    def action(self, args):
        if self.environment.user is None:
            print("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["supervisor", "administrator"]:
            print("Permission Denied")
            return

        if len(args) != 4:
            print("Invalid Arguments")
            return

        if not self.isUniqueUser(args[2]):
            print("Username is already taken.")
            return

        if not self.isValidRole(args[3]):
            print("Invalid Role")
            return

        self.environment.database.create_account(args[1], args[2], args[3])

        print("Account Created Successfully")
        return

    def isUniqueUser(self, name):
        accounts = self.environment.database.get_accounts()
        for account in accounts:
            if account["name"] == name:
                return False
        return True

    def isValidRole(self, role):
        roles = ["supervisor", "administrator", "instructor", "TA"]
        return role in roles


class DeleteAccount(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["delete_account", username]
    """
    def action(self, args):
        if self.environment.user is None:
            "Print you must be logged in to perform this action."
            return

        print("Delete Account command entered")
