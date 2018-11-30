#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
#tester le 30/10 ne fonctionne pas
#return False
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress
#import urllib2


SITE_IDENTIFIER = 'papstream'
SITE_NAME = 'PapStream'
SITE_DESC = 'Films, Séries & Mangas'

URL_MAIN = 'https://papstream.xyz/'

URL_SEARCH = ('https://papstream.xyz/rechercher', 'showMovies')

URL_SEARCH_MOVIES = ('', 'showMovies')
URL_SEARCH_SERIES = ('', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

MOVIE_NEWS = (URL_MAIN + 'dernier-films.html', 'showMovies')
MOVIE_MOVIE = (URL_MAIN + 'films.html', 'showMovies')
MOVIE_GENRES = (True, 'showGenres')

SERIE_SERIES = (URL_MAIN + 'series.html', 'showMovies')
SERIE_GENRES = (True, 'showGenresTv')

ANIM_ANIMS = (URL_MAIN + 'animes.html', 'showMovies')
ANIM_GENRES = (True, 'showGenresManga')

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIE[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIE[1], 'Films', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_ANIMS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_ANIMS[1], 'Animés', 'animes.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_GENRES[1], 'Animés (Genres)', 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        showMovies( sSearchText )
        oGui.setEndOfDirectory()
        return

def showGenres():
    oGui = cGui()

    liste = []
    liste.append( ['Action', URL_MAIN + 'films/action/'] )
    liste.append( ['Animation', URL_MAIN + 'films/animation/'] )
    liste.append( ['Aventure', URL_MAIN + 'films/aventure/'] )
    liste.append( ['Biopic', URL_MAIN + 'films/biopic/'] )
    liste.append( ['Comédie', URL_MAIN +'films/comedie/'] )
    liste.append( ['Comédie Dramatique', URL_MAIN + 'films/comedie-dramatique/'] )
    liste.append( ['Comédie Musicale', URL_MAIN + 'films/comedie-musicale/'] )
    liste.append( ['Divers', URL_MAIN + 'films/divers/'] )
    liste.append( ['Documentaire', URL_MAIN + 'films/documentaire/'] )
    liste.append( ['Drame', URL_MAIN + 'films/drame/'] )
    liste.append( ['Epouvante Horreur', URL_MAIN + 'films/epouvante-horreur/'] )
    liste.append( ['Famille', URL_MAIN + 'films/famille/'] )
    liste.append( ['Fantastique', URL_MAIN + 'films/fantastique/'] )
    liste.append( ['Guerre', URL_MAIN + 'films/guerre/'] )
    liste.append( ['Policier', URL_MAIN + 'films/policier/'] )
    liste.append( ['Romance', URL_MAIN +'films/romance/'] )
    liste.append( ['Science Fiction', URL_MAIN + '/films/science-fiction/'] )
    liste.append( ['Thriller', URL_MAIN + 'films/thriller/'] )

    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showGenresTv():
    oGui = cGui()

    liste = []
    liste.append( ['Action', URL_MAIN + 'series/action/'] )
    liste.append( ['Animation', URL_MAIN + 'series/animation/'] )
    liste.append( ['Aventure', URL_MAIN + 'series/aventure/'] )
    liste.append( ['Biopic', URL_MAIN + 'series/biopic/'] )
    liste.append( ['Comédie', URL_MAIN +'series/comedie/'] )
    liste.append( ['Comédie Dramatique', URL_MAIN + 'series/comedie-dramatique/'] )
    liste.append( ['Comédie Musicale', URL_MAIN + 'series/comedie-musicale/'] )
    liste.append( ['Divers', URL_MAIN + 'series/divers/'] )
    liste.append( ['Documentaire', URL_MAIN + 'series/documentaire/'] )
    liste.append( ['Drame', URL_MAIN + 'series/drame/'] )
    liste.append( ['Epouvante Horreur', URL_MAIN + 'series/epouvante-horreur/'] )
    liste.append( ['Famille', URL_MAIN + 'series/famille/'] )
    liste.append( ['Fantastique', URL_MAIN + 'series/fantastique/'] )
    liste.append( ['Guerre', URL_MAIN + 'series/guerre/'] )
    liste.append( ['Policier', URL_MAIN + 'series/policier/'] )
    liste.append( ['Romance', URL_MAIN +'series/romance/'] )
    liste.append( ['Science Fiction', URL_MAIN + 'series/science-fiction/'] )
    liste.append( ['Thriller', URL_MAIN + 'series/thriller/'] )

    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showGenresManga():
    oGui = cGui()

    liste = []
    liste.append( ['Action', URL_MAIN + 'animes/action/'] )
    liste.append( ['Animation', URL_MAIN + 'animes/animation/'] )
    liste.append( ['Aventure', URL_MAIN + 'animes/aventure/'] )
    liste.append( ['Biopic', URL_MAIN + 'animes/biopic/'] )
    liste.append( ['Comédie', URL_MAIN +'animes/comedie/'] )
    liste.append( ['Comédie Dramatique', URL_MAIN + 'animes/comedie-dramatique/'] )
    liste.append( ['Comédie Musicale', URL_MAIN + 'animes/comedie-musicale/'] )
    liste.append( ['Divers', URL_MAIN + 'animes/divers/'] )
    liste.append( ['Documentaire', URL_MAIN + 'animes/documentaire/'] )
    liste.append( ['Drame', URL_MAIN + 'animes/drame/'] )
    liste.append( ['Epouvante Horreur', URL_MAIN + 'animes/epouvante-horreur/'] )
    liste.append( ['Famille', URL_MAIN + 'animes/famille/'] )
    liste.append( ['Fantastique', URL_MAIN + 'animes/fantastique/'] )
    liste.append( ['Guerre', URL_MAIN + 'animes/guerre/'] )
    liste.append( ['Policier', URL_MAIN + 'animes/policier/'] )
    liste.append( ['Romance', URL_MAIN +'animes/romance/'] )
    liste.append( ['Science Fiction', URL_MAIN + 'animes/science-fiction/'] )
    liste.append( ['Thriller', URL_MAIN + 'animes/thriller/'] )

    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch = ''):
    oGui = cGui()
    oParser = cParser()
    if sSearch:
        sUrl = URL_SEARCH[0]
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)

    if sSearch:
        
        oRequestHandler.addHeaderEntry('Referer', URL_MAIN)
        oRequestHandler.addHeaderEntry('User-Agent', UA)
        # oRequestHandler.addHeaderEntry('Host', 'www.papstream.xyz')
        # oRequestHandler.addHeaderEntry('Origin', URL_MAIN)
        oRequestHandler.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
        oRequestHandler.setRequestType(cRequestHandler.REQUEST_TYPE_POST)
        oRequestHandler.addParametersLine('do=search')
        oRequestHandler.addParametersLine('subaction=search')
        oRequestHandler.addParametersLine('story=' + sSearch)
        

    sHtmlContent = oRequestHandler.request()

    sPattern = 'shortstory-in.+?<img src="([^"]+)".+?short-link"><a href="(.+?)".+?>(.+?)</a>'

    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sTitle = str(aEntry[2])
            sUrl = URL_MAIN + aEntry[1].replace('/animes/films/', '/films/').replace('/animes/series/', '/series/')
            sThumb = URL_MAIN + aEntry[0]

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            if '/series/' in sUrl or '/animes/' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showSerieSaisons', sTitle, 'series.png', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showLink', sTitle, 'films.png', sThumb, '', oOutputParameterHandler)

        progress_.VSclose(progress_)

        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    sPattern = '<div class="pages-numbers".+?<span>.+?</span><a href=["\']([^"\']+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        return URL_MAIN + aResult[1][0]

    return False

def showSerieSaisons():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sDesc = ''
    sPattern = '<div class="fstory-content.+?</h2>(.+?)<div'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if ( aResult[0] == True ):
        sDesc = aResult[1][0]

    #Decoupage pour cibler la partie des saisons
    sPattern = '<div id="full-video">(.+?)<div class="fstory-info block-p">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if ( aResult[0] == True ):
        sHtmlContent = aResult

    sPattern = '<a href="(.+?)" title=".+?(saison\s\d+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in reversed(aResult[1]):
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sUrl2   = aEntry[0]
            sSaison = aEntry[1]
            sTitle  = ("(%s) %s") % (sSaison, sMovieTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addTV(SITE_IDENTIFIER, 'ShowSerieEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()

def ShowSerieEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl   = oInputParameterHandler.getValue('siteUrl')
    sDesc  = oInputParameterHandler.getValue('sDesc')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="saision_LI2">.*?<a title="Regarder (.+?) en streaming" href=["\']([^"\']+)">'

    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sTitle = aEntry[0]
            sUrl2 = URL_MAIN + aEntry[1]

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addTV(SITE_IDENTIFIER, 'showLink', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()

def showLink():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    #if (not sDesc):
        #sPattern = '<div class=["\']fstory-content.+?</h2>(.+?)<div'
        #aResult = oParser.parse(sHtmlContent, sPattern)
        #if aResult[0]:
            #sDesc = aResult[1][0]

    sPattern = 'href="#" rel="([^"]+)".+?id="player".+?<i class="server player-.+?"></i>([^<>]+)</span>.+?<img src="([^"]+)"'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        for aEntry in aResult[1]:

            sLang  = aEntry[2].replace('/images/', '').replace('.png', '')
            #sQual  = aEntry[3].replace('(', '').replace(')', '')
            sHost  = aEntry[1].capitalize()
            sUrl2  = aEntry[0]
            sTitle = '%s [%s] [COLOR coral]%s[/COLOR]' %(sMovieTitle, sLang.upper(), sHost)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('refUrl', sUrl)
            oOutputParameterHandler.addParameter('sUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addLink(SITE_IDENTIFIER, 'showHosters', sTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    refUrl = oInputParameterHandler.getValue('refUrl')
    sUrl = oInputParameterHandler.getValue('sUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    #headers = {'User-Agent': UA, 'Referer': refUrl}

    sUrl = URL_MAIN + sUrl

    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('Referer', refUrl)
    oRequestHandler.request()
    vUrl = oRequestHandler.getRealUrl()

    #request = urllib2.Request(sUrl, None, headers)
    #reponse = urllib2.urlopen(request)
    #vUrl = reponse.geturl()
    #reponse.close()


    if vUrl:
        sHosterUrl = vUrl
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if (oHoster != False):
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
