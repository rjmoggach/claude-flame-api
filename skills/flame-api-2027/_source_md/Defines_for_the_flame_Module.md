<!-- source: Autodesk Flame Family 2027 Help _ Defines for the flame Module _ Autodesk.html -->
# Defines for the `flame` Module

Defines can be set for objects supported in the Python API. The following are just a subset of what's possible.
  **Note:

 **flame.project** was changed to **flame.projects** in the 2020.1 Update version. Both syntaxes are supported for compatibility reasons, but we encourage the use of the latter instead of the former.

| Object | Define |
|---|---|
| PyProject | <PyProject> ---> flame.projects.current_project |
| PyWorkspace | <PyWorkspace ---> flame.projects.current_project.current_workspace<br><br>or<br><br>PyProject.current_workspace |
| PyDesktop | <PyDesktop> ---> flame.projects.current_project.current_workspace.desktop<br><br>or<br><br>PyWorkspace.desktop |
| PyBatch | <PyBatch> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#]<br><br><PyBatch> ---> flame.batch (current batch) |
| PyNode | <PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].nodes[#]<br><br><PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].current_node<br><br><PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].get_node("name")<br><br><PyNode> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].create_node("type") |
| PyReelGroup | <PyReelGroup> ---> flame.projects.current_project.libraries[#].reel_groups[#]<br><br><PyReelGroup> ---> flame.projects.current_project.current_workspace.desktop.reel_groups[#] |
| PyReel | <PyReel> ---> flame.projects.current_project.current_workspace.libraries[#].reel_groups[#].reels[#]<br><br><PyReel> ---> flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#] |
| PyLibrary | <PyLibrary> ---> flame.projects.current_project.current_workspace.libraries[#] |
| PyFolder | <PyFolder> ---> flame.projects.current_project.current_workspace.libraries[#].folders[#]<br><br><PyFolder> ---> flame.projects.current_project.current_workspace.libraries[#].folders[#].folders[#] |
| PyBatchIteration | <PyBatchIteration> ---> flame.projects.current_project.current_workspace.desktop.batch_groups[#].batch_iterations[#] |
| PyClip | <PyClip> ---> flame.projects.current_project.current_workspace.libraries[#].clips[#]<br><br>flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#].clips[#] |
| PySequence | <PySequence> ---> flame.projects.current_project.current_workspace.libraries[#].sequences[#]<br><br>flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#].sequences[#] |
| PyVersion | <PyVersion> ---> PySequence.versions[#] |
| PyTimelineFX | <PyTimelineFX> ---> PyReel.sequences[#].versions[#].tracks[#].segments[#].effects[#] |
| PyTrack | <PyTrack> ---> PyReel.sequences[#].versions[#].tracks[#] |
| PyMarker | <PyMarker> ---> PyReel.sequences[#].versions[#].tracks[#].segments[#].markers[#]<br><br>PyReel.sequences[#].markers[#] |
| PyAudioTrack | <PyAudioTrack> ---> PyReel.sequences[#].audio_tracks[#] |
| PySegment | <PySegment> ---> PyReel.sequences[#].versions[#].tracks[#].segments[#] |

## Related pages

- Python API
