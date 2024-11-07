class Project:
    def __init__(self, name, description, authors, license, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license = license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, dependencies):
        return "\n".join(f"- {dep}" for dep in dependencies) if dependencies else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors:"
            f"\n{self._stringify_list(self.authors)}"
            f"\n"
            f"\nDependencies:"
            f"\n{self._stringify_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n{self._stringify_list(self.dev_dependencies)}"
        )
