from pydantic import BaseModel, Field

from composio.sdk.local_tools.lib.action import Action
from composio.sdk.local_tools.local_workspace.commons.local_docker_workspace import (get_workspace_meta_from_manager,
                                                                    communicate,
                                                                    KEY_IMAGE_NAME, KEY_CONTAINER_NAME,
                                                                    KEY_WORKSPACE_MANAGER, KEY_PARENT_PIDS)
from composio.sdk.local_tools.local_workspace.commons.utils import get_container_by_container_name
from composio.sdk.local_tools.local_workspace.commons.get_logger import get_logger

logger = get_logger()


class SearchDirRequest(BaseModel):
    workspace_id: str = Field(..., description="workspace-id to get the running workspace-manager")
    search_term: str = Field(..., description="search term to search in the directory")
    dir: str = Field(..., description="directory in which search needs to be done")


class SearchDirResponse(BaseModel):
    output: str = Field(..., description="output of the command")
    return_code: int = Field(..., description="return code for the command")


class SearchDirCmd(Action):
    """
    Moves the window down 100 lines.
    """
    _display_name = "Scroll down command on workspace"
    _request_schema = SearchDirRequest
    _response_schema = SearchDirResponse
    _tags = ["workspace"]
    script_file = "/root/commands/search.sh"
    command = "search"

    def _setup(self, args: SearchDirRequest):
        self.args = args
        self.workspace_id = args.workspace_id
        workspace_meta = get_workspace_meta_from_manager(self.workspace_id)
        self.image_name = workspace_meta[KEY_IMAGE_NAME]
        self.container_name = workspace_meta[KEY_CONTAINER_NAME]
        self.container_process = workspace_meta[KEY_WORKSPACE_MANAGER]
        self.parent_pids = workspace_meta[KEY_PARENT_PIDS]
        self.container_obj = get_container_by_container_name(self.container_name, self.image_name)
        if not self.container_obj:
            raise Exception(f"container-name {self.container_name} is not a valid docker-container")
        self.logger = logger

    def execute(self, request_data: SearchDirRequest, authorisation_data: dict) -> SearchDirResponse:
        if not request_data.dir or not request_data.dir.strip():
            raise ValueError("dir can not be null. Give a directory-name in which to search")
        self._setup(request_data)
        command = f"{self.command} {request_data.search_term} {request_data.dir}"  # Command to scroll down 100 lines
        full_command = f"source {self.script_file} && {command}"
        output, return_code = communicate(self.container_process,
                                          self.container_obj,
                                          full_command,
                                          self.parent_pids)
        return SearchDirResponse(output=output, return_code=return_code)


class SearchFileRequest(BaseModel):
    workspace_id: str = Field(..., description="workspace-id to get the running workspace-manager")
    search_term: str = Field(..., description="search term to search in the directory")
    file_name: str = Field(..., description="name of the file in which search needs to be done")


class SearchFileResponse(BaseModel):
    output: str = Field(..., description="output of the command")
    return_code: int = Field(..., description="return code for the command")


class SearchFileCmd(Action):
    """
    searches for search_term in file. If file is not provided, searches in the current open file
    """
    _display_name = "Search term in file"
    _request_schema = SearchFileRequest
    _response_schema = SearchFileResponse
    _tags = ["workspace"]
    script_file = "/root/commands/search.sh"
    command = "search_file"

    def _setup(self, args: SearchFileRequest):
        self.args = args
        self.workspace_id = args.workspace_id
        workspace_meta = get_workspace_meta_from_manager(self.workspace_id)
        self.image_name = workspace_meta[KEY_IMAGE_NAME]
        self.container_name = workspace_meta[KEY_CONTAINER_NAME]
        self.container_process = workspace_meta[KEY_WORKSPACE_MANAGER]
        self.parent_pids = workspace_meta[KEY_PARENT_PIDS]
        self.container_obj = get_container_by_container_name(self.container_name, self.image_name)
        if not self.container_obj:
            raise Exception(f"container-name {self.container_name} is not a valid docker-container")
        self.logger = logger

    def execute(self, request_data: SearchFileRequest, authorisation_data: dict) -> SearchDirResponse:
        if not request_data.file_name or not request_data.file_name.strip():
            raise ValueError("dir can not be null. Give a directory-name in which to search")
        self._setup(request_data)
        command = f"{self.command} {request_data.search_term} {request_data.file_name}"
        full_command = f"source {self.script_file} && {command}"
        output, return_code = communicate(self.container_process,
                                          self.container_obj,
                                          full_command,
                                          self.parent_pids)
        return SearchDirResponse(output=output, return_code=return_code)


class FindFileRequest(BaseModel):
    workspace_id: str = Field(..., description="workspace-id to get the running workspace-manager")
    file_name: str = Field(..., description="file-name to search for")
    dir: str = Field(..., description="name of the directory in which search needs to be done")


class FindFileResponse(BaseModel):
    output: str = Field(..., description="output of the command")
    return_code: int = Field(..., description="return code for the command")


class FindFileCmd(Action):
    """
    finds all files with the given name in dir.
    """
    _display_name = "finds file in directory"
    _request_schema = FindFileRequest
    _response_schema = FindFileResponse
    _tags = ["workspace"]
    script_file = "/root/commands/search.sh"
    command = "find_file"

    def _setup(self, args: FindFileRequest):
        self.args = args
        self.workspace_id = args.workspace_id
        workspace_meta = get_workspace_meta_from_manager(self.workspace_id)
        self.image_name = workspace_meta[KEY_IMAGE_NAME]
        self.container_name = workspace_meta[KEY_CONTAINER_NAME]
        self.container_process = workspace_meta[KEY_WORKSPACE_MANAGER]
        self.parent_pids = workspace_meta[KEY_PARENT_PIDS]
        self.container_obj = get_container_by_container_name(self.container_name, self.image_name)
        if not self.container_obj:
            raise Exception(f"container-name {self.container_name} is not a valid docker-container")
        self.logger = logger

    def execute(self, request_data: FindFileRequest, authorisation_data: dict) -> FindFileResponse:
        if not request_data.file_name or not request_data.file_name.strip():
            raise ValueError("file-name can not be null. Give a file-name to find")
        if not request_data.dir or not request_data.dir.strip():
            raise ValueError("directory in which file-name needs to be searched cant be empty. Give a directory name")
        self._setup(request_data)
        command = f"{self.command} {request_data.file_name} {request_data.dir}"
        full_command = f"source {self.script_file} && {command}"
        output, return_code = communicate(self.container_process,
                                          self.container_obj,
                                          full_command,
                                          self.parent_pids)
        return FindFileResponse(execution_output=output, return_code=return_code)