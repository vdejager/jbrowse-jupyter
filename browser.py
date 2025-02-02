from dash import html, Dash
from jbrowse_jupyter import create, create_component

app = Dash(__name__)

# create config and pass additional params
# creates an empty LGV by default when no params are passed
jbrowse_conf = create()
aliases = ["hg38"]
ref_name_aliases = {
    "adapter": {
        "type": "RefNameAliasAdapter",
        "location": {
            "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/"
            "GRCh38/hg38_aliases.txt",
        },
    },
}

# setting the assembly
assembly_data = "https://jbrowse.org/genomes/GRCh38/fasta/hg38.prefix.fa.gz"
ix = "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/hg38.ix"
ixx = "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/hg38.ixx"
meta = "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/trix/meta.json"
jbrowse_conf.set_assembly(assembly_data,
                          aliases=aliases,
                          refname_aliases=ref_name_aliases)

# add a track
track_data = "https://s3.amazonaws.com/jbrowse.org/genomes/" \
              "GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full" \
              "_analysis_set.refseq_annotation.sorted.gff.gz"
jbrowse_conf.add_track(track_data, name="test-demo", track_id="test-track")
# deleting a track
jbrowse_conf.add_track(track_data, name="delete", track_id="test-delete-track")
jbrowse_conf.delete_track("test-delete-track")
# set location
jbrowse_conf.add_text_search_adapter(ix, ixx, meta)
jbrowse_conf.set_location("10:1..19999")

# add custom theme

jbrowse_conf.set_theme("#311b92", "#0097a7", "#f57c00", "#d50000")

# grab config
config = jbrowse_conf.get_config()
jbrowse_conf.set_default_session(["test-track"])
# create a dash component

component = create_component(config)

# launch the component
app.layout = html.Div(
    [component],
    id='test'
)

if __name__ == "__main__":
    app.run_server(port=3001, debug=True)
