<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/a7maadf/DownloadsCleaner">
    <img src="/images/logo.png" alt="Logo" width="auto" height="200">
  </a>

<h3 align="center">DownloadsCleaner</h3>

  <p align="center">
    DownloadsCleaner is a utility that automatically deletes files in the Windows Downloads folder after a specified period of time passes while they are not modified, helping users maintain their system and avoid storing large amounts of unused files
    <br />
    <a href="https://github.com/a7maadf/DownloadsCleaner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/a7maadf/DownloadsCleaner">View Demo</a>
    ·
    <a href="https://github.com/a7maadf/DownloadsCleaner/issues">Report Bug</a>
    ·
    <a href="https://github.com/a7maadf/DownloadsCleaner/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#setting-up-and-using-the-portable-verison">Setting up and using the portable verison
</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

**DownloadsCleaner** is a utility that helps users maintain their system by automatically deleting files in the Windows Downloads folder after a specified period of time passes while they are not modified. By removing unused files, DownloadsCleaner helps users avoid storing large amounts of files that were intended to be used only once. With customizable options for setting expiration periods for different file types and generating log files, DownloadsCleaner is a flexible and powerful tool for keeping your system clean and organized. Plus, with the option to exclude certain files or folders from being scanned, you can ensure that important documents are never accidentally deleted. Whether you're a busy professional looking to streamline your workflow or a casual user trying to keep your system clutter-free, **DownloadsCleaner** is the perfect utility for you.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Setting up and using the portable version

- Go to the repository's [releases page](https://github.com/a7maadf/DownloadsCleaner/releases/) and download the latest release.

- Extract the downloaded files and place them in a folder other than the Downloads folder (e.g. `C:\Users\[user]\Downloads Folder Cleaner` is suggested).

- Open the `config.json` file in a text editor of your choice.

  - The config.json file contains the following
    ```
    {
      "firstSetup": true,
      "freq": -1,
      "logs": true,
      "exec": [
          "",
          ""
      ]
    }
    ```
    - "firstSetup": Indicates whether this is the first time the configuration file is being set up. Set to `false` to prevent errors when the program starts.
    - "freq": Specifies the number of days a file must go unused before it is deleted. For example, to delete files in the Downloads folder that have not been modified for 30 days, set "freq" to 30.
    - "logs": If set to true, generates log files with details about the utility's operations.
    - "exec": Lists the names of any files or folders that should be excluded from the utility's scans.

  #### Configuring the utility to start automatically on Windows boot

    1. Press the Windows key + R to open the "Run" dialog.
    2. Type `shell:startup` and press Enter. This will open the Startup folder.
    3. Place a shortcut to the utility in the Startup folder. You can create a shortcut by right-clicking on the utility's executable file and selecting "Create shortcut" from the context menu.
    4. Close the Startup folder.

    - Now, the next time you boot your computer, the utility will start automatically.

    - Note: If you want to stop the utility from starting automatically when your computer boots, simply delete the shortcut from the Startup folder.

  #### Shutting down the utility
    1. Right-click on the DownloadsCleaner icon in the system tray.
    2. From the context menu, select "Quit" to close the utility and stop it from running in the background.

    Alternatively, you can use the Task Manager to close the utility. To do so:

    1. Press the Ctrl + Alt + Delete keys simultaneously, or right-click on the taskbar and select "Task Manager" from the context menu.
    2. In the Task Manager window, go to the "Processes" tab.
    3. Find the process for the utility and select it.
    4. Click the "End task" button to close the process and shut down the utility.

  #### Accessing the log file
    To access the log file for the utility, right-click on the DownloadsCleaner icon in the system tray and select "Open logs" from the context menu. This will open the log file in a text editor, allowing you to view the details of the utility's operations.

  Alternatively, you can locate the log file manually by going to the directory where the utility is installed and looking for a file named "logs.txt". You can then open the log file with a text editor to view its contents.


<!-- USAGE EXAMPLES -->
## Usage

To configure the utility to delete files in the Downloads folder that have not been modified for 30 days, generate log files, and exclude a file named "important.docx" from being deleted, add the following to the `config.json` file:

      ```
      {
        "firstSetup": false,
        "freq": 30,
        "logs": true,
        "exec": [
            "important.docx"
        ]
      }

      ```

  Explanation:
  - "firstSetup" is set to false to prevent errors when the program starts.
  - "freq" is set to 30, which means the utility will delete any files in the Downloads folder that have not been modified for 30 days.
  - "logs" is set to true, so the utility will generate log files with details about its operations.
  - "exec" is set to a list containing "important.docx", which means the utility will exclude any files named "important.docx" from its scans and not delete them.



<!-- ROADMAP -->
## Roadmap

- [ ] An option to display notifications when the utility runs, or when it deletes specific files.
- [ ] An option to automatically empty the recycle bin when the utility runs, to further help users keep their system clean.
  - [ ] An option to specify the directories that the utility should scan for files to delete, in addition to the default Downloads folder.
- [ ] An option to specify different "freq" values for different types of files (e.g. images, documents, etc.), allowing users to set different expiration periods for different file types.

See the [open issues](https://github.com/a7maadf/DownloadsCleaner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

If you have any questions, comments, or suggestions about the DownloadsCleaner utility, please don't hesitate to contact me at [webcontact@ahmad-fawzy.com](mailto:webcontact@ahmad-fawzy.com).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/a7maadf/DownloadsCleaner.svg?style=for-the-badge
[contributors-url]: https://github.com/a7maadf/DownloadsCleaner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/a7maadf/DownloadsCleaner.svg?style=for-the-badge
[forks-url]: https://github.com/a7maadf/DownloadsCleaner/network/members
[stars-shield]: https://img.shields.io/github/stars/a7maadf/DownloadsCleaner.svg?style=for-the-badge
[stars-url]: https://github.com/a7maadf/DownloadsCleaner/stargazers
[issues-shield]: https://img.shields.io/github/issues/a7maadf/DownloadsCleaner.svg?style=for-the-badge
[issues-url]: https://github.com/a7maadf/DownloadsCleaner/issues
[license-shield]: https://img.shields.io/github/license/a7maadf/DownloadsCleaner.svg?style=for-the-badge
[license-url]: https://github.com/a7maadf/DownloadsCleaner/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
