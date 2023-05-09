from django.shortcuts import render
from django.http import HttpResponse
import gpxpy
import glob
import os
import folium
from folium.plugins import HeatMap
import xml.etree.ElementTree as ET
from gpxpy.gpx import GPX, GPXTrack, GPXTrackSegment, GPXWaypoint
from django.http import HttpResponse
from django.conf import settings
import psycopg2

def map(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
    # DB 연결 정보
    db_info = settings.DATABASES['default']
    host = db_info['HOST']
    port = db_info['PORT']
    dbname = db_info['NAME']
    user = db_info['USER']
    password = db_info['PASSWORD']

    # DB 연결
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    cur = conn.cursor()
    # mountaindew_table에서 xml_data 불러오기
    cur.execute("SELECT xml_data FROM mountaindew_table WHERE file_name LIKE '%{}%'".format(search))
    rows = cur.fetchall()
    # xml 데이터 파싱
    xml_str = rows[0][0]
    root = ET.fromstring(xml_str)
    # gpx 데이터 생성
    gpx_data = GPX()

    # gpx 데이터에 track 추가
    track = GPXTrack()
    gpx_data.tracks.append(track)

    segment = GPXTrackSegment()
    track.segments.append(segment)

    # xml 데이터에서 위도, 경도, 고도 정보 추출하여 gpx 데이터에 waypoint 추가
    for child in root.iter():
        if child.tag == '{http://www.topografix.com/GPX/1/1}trkpt':
            latitude = float(child.attrib['lat'])
            longitude = float(child.attrib['lon'])
            elevation = float(child.find('{http://www.topografix.com/GPX/1/1}ele').text)
            waypoint = GPXWaypoint(latitude=latitude, longitude=longitude, elevation=elevation)
            segment.points.append(waypoint)

    # 지도 생성
    m = folium.Map(location=[latitude, longitude], zoom_start=14)

    # HeatMap 추가
    points = [(point.latitude, point.longitude) for track in gpx_data.tracks for segment in track.segments for point in segment.points]
    HeatMap(points).add_to(m)

    # 추적 경로 그리기
    polyline = folium.PolyLine(locations=points, weight=5, color='red')
    m.add_child(polyline)

    # 지도 출력
    return HttpResponse(m._repr_html_())