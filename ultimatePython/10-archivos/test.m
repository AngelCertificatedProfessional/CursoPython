#import <MapKit/MapKit.h>
#import <UIKit/UIKit.h>
#import "ClusterViewController.h"
#import "ClusterAnnotation.h"

void ClusterIOS(void* Map_mapa,NSString* sPosicionesLat,NSString* sPosicionesLon,NSString* sTitulo,NSString* imagen,NSString* sNumeroEconomico,NSString* sColor,NSString* sColorLetra)
{
    MKMapView *tmpMap = (MKMapView*)Map_mapa;
    ClusterViewController* gc= [[ClusterViewController alloc]init];
    tmpMap.delegate= gc;
    gc.mapView = tmpMap;

    NSArray *Latitud = [[NSArray alloc]init];
    NSArray *Longitud = [[NSArray alloc]init];
    NSArray *Titulo = [[NSArray alloc]init];
    NSArray *Imagen = [[NSArray alloc]init];
    NSArray *NumeroEconomico = [[NSArray alloc]init];
    NSArray *Color = [[NSArray alloc]init];
    NSArray *ColorLetra = [[NSArray alloc]init];
    Latitud = [sPosicionesLat componentsSeparatedByString:@"/"];
    Longitud = [sPosicionesLon componentsSeparatedByString:@"/"];
    Titulo = [sTitulo componentsSeparatedByString:@"/n/"];
    Imagen = [imagen componentsSeparatedByString:@"/"];
    NumeroEconomico = [sNumeroEconomico componentsSeparatedByString:@"/"];
    Color = [sColor componentsSeparatedByString:@"/"];
    ColorLetra = [sColorLetra componentsSeparatedByString:@"/"];


    gc.Imagenes = Imagen;
    gc.Titulo = Titulo;
    gc.Latitud = Latitud;
    gc.Longitud = Longitud;
    gc.NumeroEconomico = NumeroEconomico;
    gc.Color = Color;
    gc.ColorLetra = ColorLetra;
    [gc viewDidLoad];

}

@interface ClusterViewController ()
@end
@implementation ClusterViewController
@synthesize mapView;
@synthesize numberOfLocations;
@synthesize clusteringManager;
@synthesize Imagenes;
@synthesize Titulo;
@synthesize Latitud;
@synthesize Longitud;
@synthesize NumeroEconomico;
@synthesize Color;
@synthesize ColorLetra;

- (void)viewDidLoad
{

    [super viewDidLoad];

    NSMutableArray *array = [self LocationsWithCount];
    self.numberOfLocations = Latitud.count-1;
    self.clusteringManager = [[ClusterClusteringManager alloc] initWithAnnotations:array];
    self.clusteringManager.delegate = self;
    [self.mapView showAnnotations:self.clusteringManager.allAnnotations animated:NO];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
}

#pragma mark - MKMapViewDelegate

- (void)mapView:(MKMapView *)mapView regionDidChangeAnimated:(BOOL)animated
{


[[NSOperationQueue new] addOperationWithBlock:^{
    double scale = self.mapView.bounds.size.width / self.mapView.visibleMapRect.size.width;
    NSArray *annotations = nil;
    if(scale < 0.480532){
        annotations = [self.clusteringManager clusteredAnnotationsWithinMapRect:self.mapView.visibleMapRect withZoomScale:scale];
    } else{
        annotations = self.clusteringManager.allAnnotations;
    }
    [self.clusteringManager displayAnnotations:annotations onMapView:self.mapView ];
}];

}

-(void)mapView:(MKMapView *)mapView didSelectAnnotationView:(MKAnnotationView *)view{
    MKCoordinateRegion region;
    MKCoordinateSpan span;
    region.center = view.annotation.coordinate;
    span.latitudeDelta=self.mapView.region.span.latitudeDelta /4.0002;
    span.longitudeDelta=self.mapView.region.span.longitudeDelta /4.0002;
    region.span =span;

    UIAlertView *alert = [[UIAlertView alloc]initWithTitle:@"Mapa de unidades" message:nWL_MostrarMensajeIOS(view.annotation.title) delegate:self cancelButtonTitle:@"OK" otherButtonTitles:nil, nil];
    if ([view.annotation isKindOfClass:[ClusterAnnotationCluster class]]) {
        [self.mapView setRegion:region animated:true];
    }
    else{
        [self.mapView setCenterCoordinate:view.annotation.coordinate animated:true];
        [alert show];
        [self.mapView deselectAnnotation:view.annotation animated:YES];
    }
}




- (MKAnnotationView *)mapView:(MKMapView *)mapView viewForAnnotation:(id<MKAnnotation>)annotation
{

    static NSString *const AnnotatioViewReuseID = @"AnnotatioViewReuseID";
    UILabel *label ; 

    MKAnnotationView *annotationView = (MKAnnotationView *)[self.mapView dequeueReusableAnnotationViewWithIdentifier:AnnotatioViewReuseID];
    ClusterAnnotation *an = [[ClusterAnnotation alloc] init];
    an = annotation;

    for(UIView *view in [annotationView subviews]){
        [view removeFromSuperview];
    }
    
    if (!annotationView) {
        annotationView = [[MKAnnotationView alloc] initWithAnnotation:annotation reuseIdentifier:AnnotatioViewReuseID];
    }

    if ([annotation isKindOfClass:[ClusterAnnotationCluster class]]) {
        long cont = 0;
        ClusterAnnotationCluster *cluster = (ClusterAnnotationCluster *)annotation;
        cont = (unsigned long)cluster.annotations.count;
        cluster.title = [NSString stringWithFormat:@"%lu", (unsigned long)cluster.annotations.count];
        annotationView.canShowCallout = NO;
        if(cont < 1){
            annotationView.canShowCallout = YES;
        } else if (cont >= 1 && cont <=2){
            annotationView.image= [UIImage imageNamed:@"cluster2.png"];
        }else if (cont == 3){
            annotationView.image= [UIImage imageNamed:@"cluster3.png"];
        }else if (cont == 4){
            annotationView.image= [UIImage imageNamed:@"cluster4.png"];
        }else if (cont == 5){
            annotationView.image= [UIImage imageNamed:@"cluster5.png"];
        }else if (cont == 6){
            annotationView.image= [UIImage imageNamed:@"cluster6.png"];
        }else if (cont == 7){
            annotationView.image= [UIImage imageNamed:@"cluster7.png"];
        }else if (cont == 8){
            annotationView.image= [UIImage imageNamed:@"cluster8.png"];
        }else if (cont == 9){
            annotationView.image= [UIImage imageNamed:@"cluster9.png"];
        }else if (cont >= 10 && cont < 20){
            annotationView.image= [UIImage imageNamed:@"cluster10+.png"];
        }else if (cont >= 20 && cont < 50){
            annotationView.image= [UIImage imageNamed:@"cluster20+.png"];
        }else if (cont >= 50 && cont < 100){
            annotationView.image= [UIImage imageNamed:@"cluster50+.png"];
        }else if (cont >= 100 && cont < 200){
            annotationView.image= [UIImage imageNamed:@"cluster100+.png"];
        }else if (cont >= 200){
            annotationView.image= [UIImage imageNamed:@"cluster200+.png"];
        }

    }else {
        if(an.texto.length >=1 && an.texto.length <=5){
            label = [[UILabel alloc]initWithFrame:CGRectMake(-6,-20,50,20)];
        }else if(an.texto.length > 5 && an.texto.length <= 10){
            label = [[UILabel alloc]initWithFrame:CGRectMake(-20,-20,80,20)];
        }else if(an.texto.length > 10 && an.texto.length <= 16){
            label = [[UILabel alloc]initWithFrame:CGRectMake(-40,-20,120,20)];
        }else{
            label = [[UILabel alloc]initWithFrame:CGRectMake(-40,-20,120,20)];
        }
        label.textColor = an.colorletra;
        label.font = [label.font fontWithSize:10];
        label.textAlignment = NSTextAlignmentCenter;
        label.layer.borderWidth=2.0f;
        label.layer.borderColor=an.color.CGColor;
        label.layer.backgroundColor=an.color.CGColor;
        label.layer.cornerRadius = 10.0f;
        label.text = an.texto;
        [annotationView addSubview:label];
        annotationView.image= [UIImage imageNamed:an.imagen];
        annotationView.canShowCallout = NO;
    }

    return annotationView;

}

#pragma mark - ClusterClusterManager delegate - optional

- (CGFloat)cellSizeFactorForCoordinator:(ClusterClusteringManager *)coordinator
{
    return 1.5;
}

-(UIColor *)getUIColorObjectFromHexString:(NSString *)hexStr alpha:(CGFloat)alpha{
    unsigned int hexint = [self intFromHexString:hexStr];

    UIColor *color =
    [UIColor colorWithRed:((CGFloat) ((hexint & 0xFF0000)  >> 16)) / 255
    green:((CGFloat) ((hexint & 0xFF00) >> 8))/255
    blue:((CGFloat) (hexint & 0xFF))/255
    alpha:alpha];

    return  color;
}

-(unsigned int)intFromHexString:(NSString *)hexStr{
    unsigned int hexInt = 0;

    NSScanner *scanner = [NSScanner scannerWithString:hexStr];
    [scanner setCharactersToBeSkipped:[NSCharacterSet characterSetWithCharactersInString:@"#"]];
    [scanner scanHexInt:&hexInt];

    return hexInt;
}

#pragma mark - Add annotations button action handler

- (IBAction)addNewAnnotations:(id)sender
{
    NSMutableArray *array = [self LocationsWithCount];
    [self.clusteringManager addAnnotations:array];

    self.numberOfLocations += Latitud.count-1;


    [self mapView:self.mapView regionDidChangeAnimated:NO];
}

#pragma mark - Utility

- (NSMutableArray *)LocationsWithCount
{
    NSMutableArray *array = [NSMutableArray array];
    double tmpLat ;
    double tmpLon ;
    NSString *titulo = [[NSString alloc]init];
    for (int i = 0; i < Latitud.count-1; i++) {
        tmpLat=[Latitud[i] doubleValue];
        tmpLon=[Longitud[i] doubleValue];
        titulo = Titulo[i];
        ClusterAnnotation *a = [[ClusterAnnotation alloc] init];
        UIColor *color = [self getUIColorObjectFromHexString:Color[i] alpha:.9];
        UIColor *color2= [self getUIColorObjectFromHexString:ColorLetra[i] alpha:.9];
        a.colorletra = color2;
        a.color = color;
        a.texto = NumeroEconomico[i];
        a.imagen= Imagenes[i];
        a.title= titulo;
        a.coordinate = CLLocationCoordinate2DMake(tmpLat,tmpLon);
        [array addObject:a];
    }
    return array;
}

@end