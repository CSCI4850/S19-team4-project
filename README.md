# S19-team4-project

## Demo:

### A few things to keep in mind:
1. The demo provided in the **Demo** folder was run in the Jupyter environment, but any basic Python environment will work.
2. When running `nilearn.datasets.fetch_cobre` or `nilearn.datasets.fetch_atlas_msdl`, as seen in the demo, you can specify any path as an argument to those function calls. If the dataset is not download in that path, then nilearn will download it for you, then it will refer to that path instead of downloading it again.
3. `nilearn` and `nibabel` are crucial for this demo, as they are the main packages that communicate and and test the COBRE dataset.
4. The COBRE dataset was created and is provided by by the Mind Research Network and the University of New Mexico and funded by National Institute of Health Center of Biomedical Research Excellence (COBRE) grant. Link to the offical dataset page: http://fcon_1000.projects.nitrc.org/indi/retro/cobre.html

After you have `nilearn` and `nibabel` installed, then you should be good to run the demo. The rest of the instructions and explanations are provided within the demo itself. You should just have to copy and paste the code into any Python environment to run it.