import sys
import ezdxf

def print_vtxs(dxf):
    try:
        print(f"VTX 0 => {dxf.vtx0}")
        print(f"VTX 1 => {dxf.vtx1}")
        print(f"VTX 2 => {dxf.vtx2}")
        print(f"VTX 3 => {dxf.vtx3}")
    except ezdxf.DXFAttributeError:
        print("Attribute error")

def main():
    # file = "data/AVOIDANCE_ZONE_Apr_24_2020.dxf"
    # file = "data/surface.dxf"
    file = "data/P4b_v6.5.dxf"

    try:
        print("loading file...")
        doc = ezdxf.readfile(file)
    except IOError:
        print(f"I/O error")
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print(f"Invalid of corrupted DXF file")
        sys.exit(2)

    msp = doc.modelspace()

    group = msp.groupby(dxfattrib="layer")

    a=0

    for layer, entities in group.items():
        print(f'Layer "{layer}" contains following entities ({len(entities)}):')
        for entity in entities:
            # print(f"{entity.dxftype()}")
            if entity.dxftype() == 'POINT':
                a = 1
                print(f"    {layer}")
                print(f"        {entity}")
                print(f"entity type=>        {entity.dxftype()}")
                print(entity.dxf.location)
            elif entity.dxftype() == 'POLYLINE':
                a = 1
                print(f"elevation: {entity.dxf.elevation}")
                print(f"vertices: {len(entity.vertices)}")
                for v in entity.vertices:
                    print(f" : {v.dxf.location}")
            elif entity.dxftype() == '3DFACE':
                a = 1
                print(f"vtx0: {entity.dxf.vtx0}")
                print(f"vtx1: {entity.dxf.vtx1}")
                print(f"vtx2: {entity.dxf.vtx2}")
                print(f"vtx3: {entity.dxf.vtx3}")
            elif entity.dxftype() == 'LWPOLYLINE':
                a = 1
                print(f"elevation: {entity.dxf.elevation}")
                print(f"const width: {entity.dxf.const_width}")
                for v in entity.vertices_in_wcs():
                    print(f"WCS vertex: {v}")

            else:
                print(f"{entity.dxftype()}")
        print("-"*40)

    print(len(group.items()), "item (s)")

main()