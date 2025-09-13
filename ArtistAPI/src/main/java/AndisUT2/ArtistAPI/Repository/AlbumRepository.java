package AndisUT2.ArtistAPI.Repository;

import AndisUT2.ArtistAPI.Model.Album;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class AlbumRepository {

    private final JdbcTemplate jdbcTemplate;

    private static final RowMapper<Album> albumRowMapper = (rs, rowNum) -> {
        Album album = new Album();
        album.setAlbumId(rs.getInt("album_id"));
        album.setAlbumName(rs.getString("album_name"));
        album.setArtistId(rs.getInt("artist_id"));
        return album;
    };

    public AlbumRepository(JdbcTemplate jdbcTemplate) {this.jdbcTemplate = jdbcTemplate;}

    public Album getAlbumByName(String name) {
        String sql = "select * from album where album_name = ?";
        try{
            return jdbcTemplate.queryForObject(sql, albumRowMapper, name);
        }
        catch(EmptyResultDataAccessException e){
            throw new RuntimeException("No se encontro album con el nombre " + name);
        }
    }

    public Album getAlbumById(int albumId) {
        String sql = "select * from album where album_id = ?";
        try{
            return jdbcTemplate.queryForObject(sql, albumRowMapper, albumId);
        }
        catch(EmptyResultDataAccessException e){
            throw new RuntimeException("No se encontro album con el nombre " + albumId);
        }
    }

    public List<Album> getAllAlbums() {
        String sql = "select * from album";
        return jdbcTemplate.query(sql, albumRowMapper);
    }

    public List<Album> getAlbumsByArtistId(int artistId) {
        String sql = "select * from album where artist_id = ?";
        return jdbcTemplate.query(sql, albumRowMapper, artistId);
    }

    public Album saveAlbum(Album album) {
        String sql = "insert into album (album_name, artist_id) values (?, ?)";
        return getAlbumById(album.getAlbumId());
    }

}
