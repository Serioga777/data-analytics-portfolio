"""
File Operations Tool for Agents
"""
from typing import Dict, Any, Optional
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


class FileOperationsTool:
    """Tool for file operations (read, write, list)"""
    
    def __init__(self, base_path: Optional[str] = None):
        """
        Initialize file operations tool
        
        Args:
            base_path: Base directory path for operations
        """
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.name = "file_operations"
        self.description = "Perform file operations (read, write, list files)"
    
    def read_file(self, file_path: str) -> Dict[str, Any]:
        """
        Read a file
        
        Args:
            file_path: Path to file
            
        Returns:
            File content and metadata
        """
        try:
            full_path = self.base_path / file_path
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            logger.info(f"Read file: {file_path}")
            return {
                'success': True,
                'content': content,
                'path': str(full_path),
                'size': len(content)
            }
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return {
                'success': False,
                'error': str(e),
                'path': file_path
            }
    
    def write_file(self, file_path: str, content: str) -> Dict[str, Any]:
        """
        Write content to a file
        
        Args:
            file_path: Path to file
            content: Content to write
            
        Returns:
            Operation result
        """
        try:
            full_path = self.base_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Wrote file: {file_path}")
            return {
                'success': True,
                'path': str(full_path),
                'size': len(content)
            }
        except Exception as e:
            logger.error(f"Error writing file {file_path}: {e}")
            return {
                'success': False,
                'error': str(e),
                'path': file_path
            }
    
    def list_files(self, directory: str = ".", pattern: str = "*") -> Dict[str, Any]:
        """
        List files in a directory
        
        Args:
            directory: Directory to list
            pattern: File pattern (glob)
            
        Returns:
            List of files
        """
        try:
            full_path = self.base_path / directory
            files = list(full_path.glob(pattern))
            
            logger.info(f"Listed files in: {directory}")
            return {
                'success': True,
                'files': [str(f.relative_to(self.base_path)) for f in files],
                'count': len(files)
            }
        except Exception as e:
            logger.error(f"Error listing files in {directory}: {e}")
            return {
                'success': False,
                'error': str(e),
                'directory': directory
            }
    
    def __call__(self, operation: str, **kwargs) -> Dict[str, Any]:
        """Make the tool callable"""
        operations = {
            'read': self.read_file,
            'write': self.write_file,
            'list': self.list_files
        }
        
        if operation in operations:
            return operations[operation](**kwargs)
        else:
            return {'success': False, 'error': f'Unknown operation: {operation}'}
