from homeassistant import config_entries, core

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from homeassistant.exceptions import ConfigEntryAuthFailed, Unauthorized

from .const import DOMAIN

from homeassistant.const import CONF_HOST, Platform

from .mertik import Mertik

from .mertikdatacoordinator import MertikDataCoordinator


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    mertik = Mertik(entry.data[CONF_HOST])

    """Set up the Mertik component."""
    coordinator = MertikDataCoordinator(hass, mertik)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Forward the setup to the sensor platform.
    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SWITCH])

    return True


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    return True
