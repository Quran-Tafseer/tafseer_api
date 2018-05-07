# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)


## [1.2.0](https://github.com/EmadMokhtar/tafseer_api/milestone/3) - 2018-03-03

### Added
- Add the next ayah in Tafseer endpoint response header `X-Next-Ayah`.
- Logging.
- Add more meta data (language, book name, and author) to Tafseer endpoint.
- Get list of Tafseer by language. 


## [1.1.0](https://github.com/EmadMokhtar/tafseer_api/milestone/2) - 2018-01-14

### Added
- Ayah Tafseer by range of ayat in the chapter endpoint.

### Fixed
- Performance improvement.
- Return 404 status code in case of requesting tafseer not found.


## [1.0.0](https://github.com/EmadMokhtar/tafseer_api/milestone/1) - 2017-12-17

### Added
- Implement the Tafseer API.
- Test suite.
- Deployment on Heroku.
- Added a English and Arabic documentation.