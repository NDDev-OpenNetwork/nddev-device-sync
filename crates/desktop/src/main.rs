use nddev_device_sync_application::builtin_graph;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let graph = builtin_graph()?;
    let modules: Vec<_> = graph.iter().collect();
    println!("{}", serde_json::to_string_pretty(&modules)?);
    Ok(())
}
