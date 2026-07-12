"""
Plugins: A modular plugin system for SmartGen Docs.

This module provides a plugin architecture that allows features like
API Reference, Changelog, and Guides to be treated as optional plugins.
"""

import os
import yaml
from typing import Dict, List, Any, Callable
from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base class for all SmartGen Docs plugins.
    """
    
    def __init__(self, name: str, enabled: bool = True):
        """
        Initialize a plugin.
        
        Args:
            name: Name of the plugin
            enabled: Whether the plugin is enabled
        """
        self.name = name
        self.enabled = enabled
    
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """
        Initialize the plugin with configuration.
        
        Args:
            config: Configuration dictionary from smartgen.yml
        """
        pass
    
    @abstractmethod
    def execute(self) -> None:
        """Execute the plugin's main functionality."""
        pass
    
    def get_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get plugin-specific configuration.
        
        Args:
            config: Main configuration dictionary
        
        Returns:
            Plugin-specific configuration
        """
        plugins_config = config.get('plugins', {})
        return plugins_config.get(self.name, {})


class PluginManager:
    """
    Manages registration, loading, and execution of plugins.
    """
    
    def __init__(self):
        """Initialize the plugin manager."""
        self.plugins: Dict[str, Plugin] = {}
        self.hooks: Dict[str, List[Callable]] = {}
    
    def register(self, plugin: Plugin) -> None:
        """
        Register a plugin.
        
        Args:
            plugin: Plugin instance to register
        """
        self.plugins[plugin.name] = plugin
    
    def register_hook(self, hook_name: str, callback: Callable) -> None:
        """
        Register a hook callback.
        
        Args:
            hook_name: Name of the hook
            callback: Callback function
        """
        if hook_name not in self.hooks:
            self.hooks[hook_name] = []
        self.hooks[hook_name].append(callback)
    
    def execute_hook(self, hook_name: str, *args, **kwargs) -> List[Any]:
        """
        Execute all callbacks for a hook.
        
        Args:
            hook_name: Name of the hook
            *args: Positional arguments for callbacks
            **kwargs: Keyword arguments for callbacks
        
        Returns:
            List of results from callbacks
        """
        results = []
        if hook_name in self.hooks:
            for callback in self.hooks[hook_name]:
                results.append(callback(*args, **kwargs))
        return results
    
    def initialize_all(self, config: Dict[str, Any]) -> None:
        """
        Initialize all registered plugins.
        
        Args:
            config: Configuration dictionary
        """
        for plugin in self.plugins.values():
            if plugin.enabled:
                plugin.initialize(config)
    
    def execute_all(self) -> None:
        """Execute all enabled plugins."""
        for plugin in self.plugins.values():
            if plugin.enabled:
                plugin.execute()
    
    def get_plugin(self, name: str) -> Plugin:
        """
        Get a plugin by name.
        
        Args:
            name: Name of the plugin
        
        Returns:
            Plugin instance or None if not found
        """
        return self.plugins.get(name)
    
    def is_enabled(self, name: str) -> bool:
        """
        Check if a plugin is enabled.
        
        Args:
            name: Name of the plugin
        
        Returns:
            True if plugin is enabled, False otherwise
        """
        plugin = self.plugins.get(name)
        return plugin.enabled if plugin else False


class APIReferencePlugin(Plugin):
    """
    Plugin for auto-generating API reference documentation.
    """
    
    def __init__(self):
        """Initialize the API Reference plugin."""
        super().__init__('api-reference', enabled=True)
        self.config = {}
    
    def initialize(self, config: Dict[str, Any]) -> None:
        """Initialize the API Reference plugin."""
        self.config = self.get_config(config)
    
    def execute(self) -> None:
        """Execute API reference generation."""
        if not self.enabled:
            return
        
        # Implementation would go here
        pass


class ChangelogPlugin(Plugin):
    """
    Plugin for rendering changelog from JSON.
    """
    
    def __init__(self):
        """Initialize the Changelog plugin."""
        super().__init__('changelog', enabled=True)
        self.config = {}
    
    def initialize(self, config: Dict[str, Any]) -> None:
        """Initialize the Changelog plugin."""
        self.config = self.get_config(config)
    
    def execute(self) -> None:
        """Execute changelog rendering."""
        if not self.enabled:
            return
        
        # Implementation would go here
        pass


class GuidesPlugin(Plugin):
    """
    Plugin for managing guides and tutorials.
    """
    
    def __init__(self):
        """Initialize the Guides plugin."""
        super().__init__('guides', enabled=True)
        self.config = {}
    
    def initialize(self, config: Dict[str, Any]) -> None:
        """Initialize the Guides plugin."""
        self.config = self.get_config(config)
    
    def execute(self) -> None:
        """Execute guides processing."""
        if not self.enabled:
            return
        
        # Implementation would go here
        pass


# Global plugin manager instance
_plugin_manager = None


def get_plugin_manager() -> PluginManager:
    """
    Get the global plugin manager instance.
    
    Returns:
        PluginManager instance
    """
    global _plugin_manager
    if _plugin_manager is None:
        _plugin_manager = PluginManager()
        
        # Register built-in plugins
        _plugin_manager.register(APIReferencePlugin())
        _plugin_manager.register(ChangelogPlugin())
        _plugin_manager.register(GuidesPlugin())
    
    return _plugin_manager
