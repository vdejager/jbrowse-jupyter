## JBrowse Jupyter vs Other tools

| Features                                            | JBrowse/ JBrowse Jupyter | IGV.js /igv-notebook | ipyIgv      | Gosling/Gos | D3GB        | PygBrowse | Mango       |
| --------------------------------------------------- | ------------------------ | -------------------- | ----------- | ----------- | ----------- | --------- | ----------- |
| Binder support                                      | &#x2611;                 | &#x2611;             | &#x2611;    | &#x2611;    | &#x2612;    | &#x2612;  | &#x2612;    |
| Colab support                                       | &#x2611;                 | &#x2611;             | &#x2612;    | &#x2611;    | &#x2612;    | &#x2612;  | &#x2612;    |
| Custom Color Theming                                | &#x2611;                 | &#x2612;             | &#x2612;    | &#x2611;    | &#x2612;    | &#x2612;  | &#x2612;    |
| Deletion of tracks                                  | &#x2611;                 | &#x2612;             | &#x2611;    | &#x2612;    | &#x2612;    | &#x2612;  | &#x2612;    |
| Export view as SVG                                  | &#x2611; \*              | &#x2611;             | &#x2611;    | &#x2612;    | &#x2612;    | &#x2612;  | &#x2611;    |
| Local file support                                  | &#x2611; \*\*            | &#x2611;             | &#x2611;    | &#x2611;    | &#x2611;    | &#x2611;  | &#x2611;    |
| Supports Circular Genome View                       | &#x2611;                 | &#x2612;             | &#x2612;    | &#x2611;    | &#x2612;    | &#x2612;  | &#x2612;    |
| Ability to enable text searching from indexed files | &#x2611;                 | &#x2612;             | &#x2612;    | &#x2612;    | &#x2612;    | &#x2612;  | &#x2612;    |
| Ability to add tracks from Dataframes               | &#x2611;                 | &#x2612;             | &#x2612;    | &#x2612;    | &#x2612;    | &#x2611;  | &#x2612;    |
| Zooming in on regions of interest                   | &#x2611; \*              | &#x2611;             | &#x2611; \* | &#x2611; \* | &#x2611; \* | &#x2612;  | &#x2611; \* |

\* Feature is accessible via the component's UI and not by API. \*\* Path
support for local files is only available when running notebook in Jupyter lab
and Jupyter notebook. Local file support in colab and binder is available by
running the JBrowse dev server to host your data and creating urls to pass to
the JBrowse view.

- For more features of the JBrowse and JBrowse embedded components checkout
  [our documentation](https://jbrowse.org/jb2/docs/embedded_components/)
- Igv.js [documentation](https://github.com/igvteam/igv.js/wiki/)
- igv-notebook [documentation](https://github.com/igvteam/igv-notebook)
- ipyIgv [documentation](https://github.com/QuantStack/ipyigv)
- D3GB [documentation](http://d3gb.usal.es/index.html)
- PygBrowse [documentation](https://github.com/phageghost/python-genome-browser)
- Gosling [documentation](https://github.com/gosling-lang/gosling.js)
- Gos [documentation](https://gosling-lang.github.io/gos/)
- Mango
  [documentation](https://bdg-mango.readthedocs.io/en/latest/jupyterWidgets/usage.html)
