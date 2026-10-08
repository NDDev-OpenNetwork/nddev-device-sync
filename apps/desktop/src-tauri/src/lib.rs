use nddev_device_sync_application::builtin_modules;
use nddev_device_sync_domain::ModuleDescriptor;

#[tauri::command]
fn list_modules() -> Result<Vec<ModuleDescriptor>, String> {
    Ok(builtin_modules())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![list_modules])
        .run(tauri::generate_context!())
        .expect("error while running nddev-device-sync");
}
